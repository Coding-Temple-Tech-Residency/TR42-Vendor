-- SQLite

-- select 
--     u.first_name, 
--     u.last_name,
--     u.is_admin,
--     vu.role,
--     v.company_name
-- from user u
-- inner join vendor_user vu
-- using (user_id)
-- inner join vendor v
-- using (vendor_id)
-- limit 10;

-- Total Number of tickets per vendor

-- select v.company_name, count(t.ticket_id)
-- from vendor v
-- inner join work_orders wo
-- on v.vendor_id = wo.assigned_vendor
-- inner join ticket t
-- on wo.work_order_id = t.work_order_id
-- group by v.company_name
-- order by 2 desc;

-- -- Number of active tickets
-- select v.company_name, count(t.ticket_id)
-- from vendor v
-- inner join work_orders wo
-- on v.vendor_id = wo.assigned_vendor
-- inner join ticket t
-- on wo.work_order_id = t.work_order_id
-- where t.status = 'completed'
-- group by v.company_name
-- order by 2 desc;

-- number of submitted invoices by vendor
-- select v.company_name, count(i.invoice_id)
-- from invoice i
-- join line_item li
-- using (invoice_id)
-- join vendor v
-- using (vendor_id)
-- where i.invoice_status = 'submitted'
-- group by 1;

-- select ticket_id, created_at, completed_at, assigned_at, due_date, start_time
-- from ticket
-- where completed_at is not null and due_date < completed_at
-- limit 10;

-- Vendor average Completion time

-- select 
--     v.company_name,
--     avg(julianday(t.completed_at) - julianday(t.assigned_at)) as avg_ticket_completion_time
-- from ticket t
-- join vendor v
-- using(vendor_id)
-- where t.completed_at >= datetime('now', '-30 days')
-- group by 1
-- order by 2 desc;


-- select 
--     v.company_name,
--     avg(julianday(t.completed_at) - julianday(t.assigned_at)) as avg_ticket_completion_time
-- from ticket t
-- join vendor v
-- using(vendor_id)
-- where t.completed_at >= datetime('now', '-60 days')
--   and t.completed_at < datetime('now', '-30 days')
-- group by 1
-- order by 2 desc;

-- Unassigned work orders by well

-- select 
--     w.well_name, 
--     count(wo.work_order_id),
--     (
--         select count(*) 
--         from work_orders 
--         where current_status='unassigned'
--     ) as 'total unassigned'
-- from work_orders wo
-- join well w
-- using (well_id)
-- where current_status = 'unassigned'
-- group by well_id
-- order by 2 desc;

-- Tickets in progress
-- select v.vendor_code, count(*) as 'tickets in progress'
-- from ticket t
-- join vendor v
-- using (vendor_id)
-- where t.status='in progress'
-- group by vendor_id;

-- Tickets Completed by Vendor
-- select v.company_name, count(*) 
-- from ticket t
-- join vendor v
-- using(vendor_id)
-- where t.status='completed'
-- group by 1;

-- select 
--     status,
--     completed_at
-- from ticket
-- limit 20;

-- Invoices

-- select invoice_id, count(*), i.total_amount, sum(li.amount)
-- from invoice i
-- join line_item li
-- using (invoice_id)
-- where i.invoice_status = 'paid'
-- group by invoice_id;

-- Contractor Performance

-- select * from vendor
-- limit 1;

-- Test Vendor: 3c0d000d-535b-4008-bf4a-7d351976d8cd

-- Contractor Performance

-- select 
--     vc.full_name,
--     round(avg(cp.rating), 2),
--     count(cp.ticket_id)
-- from 
-- (
-- select 
--     c.contractor_id,
--     u.first_name || " " || u.last_name as full_name
-- from contractors c
-- join user u
-- using (user_id)
-- where vendor_id = '3c0d000d-535b-4008-bf4a-7d351976d8cd'
-- ) as vc
-- join contractor_performance cp
-- using (contractor_id)
-- group by 1
-- order by 2 desc;

-- select v.company_name, round(cp.avg_rating, 2)
-- from (
--     select c.vendor_id, avg(cp.rating) as avg_rating
--     from contractor_performance cp
--     join contractors c using (contractor_id)
--     group by c.vendor_id
-- ) cp
-- join vendor v using (vendor_id)
-- order by cp.avg_rating desc;

-- On time Delivery by Vendor

-- select 
--     v.company_name,
--     round(avg(
--         case 
--             when (t.completed_at > t.due_date) or (t.completed_at is null and t.due_date < '2026-03-01')
--             then 0
--             else 1
--         end
--     ) * 100, 2) as on_time,
--     count(t.ticket_id) as ticket_count
-- from ticket t
-- join vendor v using (vendor_id)
-- where t.created_at between '2025-11-01' and '2026-03-01'
-- group by v.vendor_id
-- order by on_time desc;

-- select 
--     v.company_name,
--     round(avg(
--         case 
--             when (t.completed_at > t.due_date) or (t.completed_at is null and t.due_date < date('now'))
--             then 0
--             else 1
--         end
--     ) * 100, 2) as on_time,
--     count(t.ticket_id) as ticket_count
-- from ticket t
-- join vendor v using (vendor_id)
-- where t.created_at between '2025-11-01' and date('now')
-- group by v.vendor_id
-- order by on_time desc;

-- Contractor Utilization Rate (across vendors)
-- SELECT 
--     c.contractor_id, 
--     u.first_name || ' ' || u.last_name AS full_name, 
--     COUNT(t.ticket_id) AS ticket_count,
--     AVG(COUNT(t.ticket_id)) OVER () AS avg_ticket_per_contractor,
--     COUNT(t.ticket_id) * 1.0 / AVG(COUNT(t.ticket_id)) OVER () AS workload_ratio
-- FROM ticket t
-- JOIN contractors c
--     ON t.assigned_contractor = c.contractor_id
-- JOIN user u
--     ON c.user_id = u.user_id
-- GROUP BY c.contractor_id, u.first_name, u.last_name
-- order by 5 desc;

-- select * from ticket limit 10

-- Work Orders by Vendor

select 
    work_order_id, current_status, completed_at
from work_orders
where current_status = 'completed';