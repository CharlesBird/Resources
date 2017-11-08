利润报表
select lm.id, lm.date2 + interval '8 hours' as date, extract(year from lm.date2 + interval '8 hours')::varchar(4) as year, extract(month from lm.date2 + interval '8 hours')::varchar(2) as month, lm.product_id, lm.brand_id, case when lc.picking = 't' then lc.profit*(lm.actual_qty/lc.qty_delivered) else lc.profit*(lm.actual_qty/lc.actual_qty) end as profit from logistics_move lm left join linyan_contract lc on lm.contract_id2 = lc.id where lm.state = 'done' and lm.contract_id2 is not null;


现金流
select COALESCE(t1.rece_invoice, 0.0) as rece_invoice, -1*COALESCE(t2.pay_invoice, 0.0) as pay_invoice, -1*COALESCE(t3.rece_payment, 0.0) as rece_payment, COALESCE(t4.pay_payment, 0.0) as pay_payment, COALESCE(t1.rece_invoice, 0.0)-COALESCE(t3.rece_payment, 0.0)-COALESCE(t2.pay_invoice, 0.0)+COALESCE(t3.rece_payment, 0.0) as amount from (select 1 as rel_id, sum(residual) as rece_invoice from linyan_invoice where invoice_type = 'out_invoice' and date_invoice < '2017-06-25') t1 left join (select 1 as rel_id, sum(residual) as pay_invoice from linyan_invoice where invoice_type = 'in_invoice' and date_invoice < '2017-06-25') t2 on t1.rel_id = t2.rel_id left join (select 1 as rel_id, sum(remaining_amount) as rece_payment from linyan_payment where payment_type = 'inbound' and payment_date < '2017-06-25') t3 on t1.rel_id = t3.rel_id left join (select 1 as rel_id, sum(remaining_amount) as pay_payment from linyan_payment where payment_type = 'outbound' and payment_date < '2017-06-25') t4 on t1.rel_id = t4.rel_id

select 1 as rel_id, sum(residual) as pay_invoice from linyan_invoice where invoice_type = 'in_invoice' and date_invoice < '2017-06-25';

select 1 as rel_id, sum(remaining_amount) as rece_payment from linyan_payment where payment_type = 'inbound' and payment_date < '2017-06-25';

select 1 as rel_id, sum(remaining_amount) as pay_payment from linyan_payment where payment_type = 'outbound' and payment_date < '2017-06-25';