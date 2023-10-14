# SELECT order_id, product_id, DATE_FORMAT(out_date, '%Y-%m-%d') as out_date,
# CASE WHEN OUT_DATE is NULL THEN '출고미정'
# else CASE WHEN OUT_DATE > '2022-05-01' THEN '출고대기'
# else '출고완료'
# end end as '출고여부'
# FROM FOOD_ORDER
# ORDER BY order_id ASC;


SELECT ORDER_ID, PRODUCT_ID, DATE_FORMAT(OUT_DATE, "%Y-%m-%d") AS OUT_DATE,
CASE WHEN OUT_DATE <= '2022-05-01' THEN '출고완료'
    ELSE CASE WHEN OUT_DATE IS NOT NULL THEN '출고대기'
    ELSE '출고미정'
    END END AS '출고여부'
FROM FOOD_ORDER
ORDER BY ORDER_ID