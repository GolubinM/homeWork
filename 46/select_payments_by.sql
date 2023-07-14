SELECT cpt.title name,
       cts.contr_date contract_date,
       cts.summ contract_summ,
       sum(pm.summ) total_pyaments
  FROM contracts cts
       JOIN
       counterparty cpt ON cpt.count_id = cts.count_id
       JOIN
       payments pm ON cts.contr_id = pm.contr_id
 WHERE cts.contr_date > date("2022-04-01")
 GROUP BY cpt.count_id
HAVING sum(pm.summ) > 1000000;
