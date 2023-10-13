SELECT I.REST_ID, REST_NAME, FOOD_TYPE, FAVORITES, ADDRESS, ROUND(AVG(REVIEW_SCORE), 2) AS SCORE
FROM REST_INFO I
RIGHT JOIN REST_REVIEW SC on I.REST_ID = SC.REST_ID
WHERE ADDRESS LIKE "서울%"
GROUP BY I.REST_ID
ORDER BY SCORE DESC, FAVORITES DESC



