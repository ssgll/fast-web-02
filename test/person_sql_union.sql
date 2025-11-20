SELECT
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
  LY_ODS.ODS_RSXT_YXSYHR_RETA10 t1
LEFT JOIN LY_ODS.ODS_RSXT_YXSYHR_RETA01 t2 ON
  t1.a0100 = t2.A0100 WHERE T2.E0127 IS NOT NULL
UNION ALL
SELECT
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
  LY_ODS.ODS_RSXT_YXSYHR_FPKA10 t1
LEFT JOIN LY_ODS.ODS_RSXT_YXSYHR_FPKA01 t2 ON
  t1.a0100 = t2.A0100 WHERE T2.E0127 IS NOT NULL
UNION ALL
SELECT
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
  LY_ODS.ODS_RSXT_YXSYHR_TPKA10 t1
LEFT JOIN LY_ODS.ODS_RSXT_YXSYHR_TPKA01 t2 ON
  t1.a0100 = t2.A0100 WHERE T2.E0127 IS NOT NULL
UNION ALL
SELECT
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
  LY_ODS.ODS_RSXT_YXSYHR_USRA10 t1
LEFT JOIN LY_ODS.ODS_RSXT_YXSYHR_USRA01 t2 ON
  t1.a0100 = t2.A0100 WHERE T2.E0127 IS NOT NULL
UNION ALL
SELECT
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
  LY_ODS.ODS_RSXT_YXSYHR_HTKA10 t1
LEFT JOIN LY_ODS.ODS_RSXT_YXSYHR_HTKA01 t2 ON
  t1.a0100 = t2.A0100 WHERE T2.E0127 IS NOT NULL
UNION ALL
SELECT
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
  LY_ODS.ODS_RSXT_YXSYHR_OTHA10 t1
LEFT JOIN LY_ODS.ODS_RSXT_YXSYHR_OTHA01 t2 ON
  t1.a0100 = t2.A0100 WHERE T2.E0127 IS NOT NULL
UNION ALL
SELECT
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
  LY_ODS.ODS_RSXT_YXSYHR_TRSA10 t1
LEFT JOIN LY_ODS.ODS_RSXT_YXSYHR_TRSA01 t2 ON
  t1.a0100 = t2.A0100 WHERE T2.E0127 IS NOT NULL
UNION ALL
SELECT
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
  LY_ODS.ODS_RSXT_YXSYHR_WPKA10 t1
LEFT JOIN LY_ODS.ODS_RSXT_YXSYHR_WPKA01 t2 ON
  t1.a0100 = t2.A0100 WHERE T2.E0127 IS NOT NULL
UNION ALL
SELECT
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
  LY_ODS.ODS_RSXT_YXSYHR_TSKA10 t1
LEFT JOIN LY_ODS.ODS_RSXT_YXSYHR_TSKA01 t2 ON
  t1.a0100 = t2.A0100 WHERE T2.E0127 IS NOT NULL
UNION ALL
SELECT
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
  LY_ODS.ODS_RSXT_YXSYHR_LZKA10 t1
LEFT JOIN LY_ODS.ODS_RSXT_YXSYHR_LZKA01 t2 ON
  t1.a0100 = t2.A0100 WHERE T2.E0127 IS NOT NULL
UNION ALL
SELECT
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
  LY_ODS.ODS_RSXT_YXSYHR_TEMA10 t1
LEFT JOIN LY_ODS.ODS_RSXT_YXSYHR_TEMA01 t2 ON
  t1.a0100 = t2.A0100 WHERE T2.E0127 IS NOT NULL