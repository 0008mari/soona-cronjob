SELECT C.*, S.tchr_id
FROM school C
    INNER JOIN student S
    ON S.sch_id = C.sch_id
