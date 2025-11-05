from typing import Optional,Any,List
from pydantic import BaseModel,Field
from datetime import datetime


# 基础响应模型
class BaseResponse(BaseModel):
    code: int = Field(default=200,description="状态码")
    msg: str = Field(default="Success",description="响应消息")
    timestamp: str = Field(default=datetime.now().isoformat(),description="时间戳")

    model_config = {"arbitrary_types_allowed":True}

# 数据响应模型
class DataResponse(BaseResponse):
    data: Optional[Any] = Field(None, description="响应数据")

# 列表响应模型
class ListDataResponse(BaseResponse):
    data: List[Any] = Field(default_factory=list,description="列表数据")
    total: int = Field(default=0,description="数据总数")

# 分页响应模型
class PageResponse(BaseResponse):
    data: List[Any] = Field(default_factory=list,description="分页数据")
    total: int = Field(default=0,description="总记录数")
    page: int = Field(default=1,description="当前页码")
    page_size:int = Field(default=10,description="分页大小")
    total_pages: int = Field(default=1,description="总页数")

# 错误响应模型
class ErrorResponse(BaseResponse):
    error_code:Optional[str] = Field(default=None,description="错误代码")
    details: Optional[str] = Field(default=None,description="错误详情")

# 响应工厂类
class ResponseFactory:
    """用于生成统一格式响应的工厂类"""

    @staticmethod
    def success(data: Any=None,msg:str="操作成功")->DataResponse:
        return DataResponse(msg=msg,data=data)

    @staticmethod
    def list_success(data: Optional[List[Any]] = None,msg:str="查询成功")->ListDataResponse:
        data_list = data or []
        return ListDataResponse(data=data_list,total=len(data_list),msg=msg)

    @staticmethod
    def page_success(
            data: Optional[List[Any]] = None,
            total: int = 0,
            page: int = 1,
            page_size: int = 10,
            msg:str="查询成功"
    )->PageResponse:
        data_list = data or []
        total_pages = (total + page_size - 1) // page_size if page_size > 0 else 0

        return PageResponse(
            data=data_list,
            total=total,
            page=page,
            page_size=page_size,
            total_pages=total_pages,
            msg=msg
        )

    @staticmethod
    def error(code:int = 400, msg:str="操作失败",error_code:Optional[str]=None,details:Any=None)->ErrorResponse:
        # 确保details是字符串类型
        details_str = str(details) if details is not None else None
        return ErrorResponse(code=code,msg=msg,error_code=error_code,details=details_str)