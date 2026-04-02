-- SQLite

-- Total Number of tickets per vendor

select v.company_name, count(t.ticket_id)
from vendor v
inner join work_orders wo
on v.vendor_id = wo.assigned_vendor
inner join ticket t
on wo.work_order_id = t.work_order_id
group by v.company_name
order by 2 desc;

-- Number of active tickets
select v.company_name, count(t.ticket_id)
from vendor v
inner join work_orders wo
on v.vendor_id = wo.assigned_vendor
inner join ticket t
on wo.work_order_id = t.work_order_id
where t.status = 'completed'
group by v.company_name
order by 2 desc;
