# SELECT apnt_no, pt_name, p.pt_no, d.mcdp_cd, dr_name, apnt_ymd 
# FROM APPOINTMENT a
# INNER JOIN PATIENT p on p.pt_no = a.pt_no
# INNER JOIN DOCTOR d on d.dr_id = a.mddr_id
# WHERE YEAR(apnt_ymd) = 2022 and MONTH(apnt_ymd) = 4 and DAY(apnt_ymd) = 13
# and apnt_cncl_yn = 'N' and d.mcdp_cd = 'CS'
# ORDER BY apnt_ymd

SELECT APNT_NO,	PT_NAME, A.PT_NO, A.MCDP_CD, DR_NAME, APNT_YMD
FROM APPOINTMENT A
JOIN PATIENT P ON A.PT_NO = P.PT_NO
JOIN DOCTOR D ON DR_ID = MDDR_ID
WHERE APNT_YMD LIKE "2022-04-13%" AND APNT_CNCL_YN = 'N' AND A.MCDP_CD = 'CS'
ORDER BY APNT_YMD