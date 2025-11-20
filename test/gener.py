def generate_person_type_sql():
    """
    生成包含所有人员类型的SQL查询语句
    """
    # 人员类型列表
    person_types = [
        "RET", "FPK", "TPK", "USR", "HTK",
        "OTH", "TRS", "WPK", "TSK", "LZK", "TEM"
    ]

    # 基础SQL模板
    sql_template = """SELECT
  t2.E0127 AS JGH,
  t1.I9999 AS sxh,
  -- 顺序号
  to_char(t1.A1015, 'yyyyMMdd') AS FZRQ,
  -- 发证日期 
  t1.A1020 AS ZYJSZCM,
  --聘任专业技术职务名称
  t1.C1005 AS zcdj,
  --职 称 等 级 
  T1.E1013 AS PSJG,
  --评审机构
  T1.A1010 AS QDZGTJM,
  --取得资格途径码,
  RPAD(T1.A1005, 3, '0') AS ZYJSZWM,
  --专业技术职务码
  to_char(t1.A1025, 'yyyyMMdd') AS PRQSSJ,
  --聘任起始时间
  to_char(t1.A1030, 'yyyyMMdd') AS PRZZSJ,
  --聘任终止时间
  decode(t1.H1001, '1', '1', '2', '0') AS SFJYZYZG
  --是否具有职业资格
FROM
  LY_ODS.ODS_RSXT_YXSYHR_{}A10 t1
LEFT JOIN LY_ODS.ODS_RSXT_YXSYHR_{}A01 t2 ON
  t1.a0100 = t2.A0100 WHERE T2.E0127 IS NOT NULL"""

    # 使用列表推导式生成所有SQL片段
    sql_fragments = []
    for p_type in person_types:
        sql_fragments.append(sql_template.format(p_type, p_type))

    # 用UNION ALL连接所有查询
    full_query = "\nUNION ALL\n".join(sql_fragments)

    return full_query


if __name__ == "__main__":
    # 测试函数
    sql_result = generate_person_type_sql()
    print("生成的SQL语句长度:", len(sql_result))
    print("包含的人员类型数量: 11")

    # 写入文件
    with open("person_sql_union.sql", "w", encoding="utf-8") as f:
        f.write(sql_result)
    print("SQL已写入文件: person_sql_union.sql")

    person_types = [
        "RET", "FPK", "TPK", "USR", "HTK",
        "OTH", "TRS", "WPK", "TSK", "LZK", "TEM"
    ]
    for i in person_types:
        print(i+"A10")