use parkingsys;

-- 插入一个停车场实体记录-----------------------parkinglot停车场表------------------------------------------
insert into parkinglot(address, total_space, remain_space, charing_standard)
values ('商业大厦', 100, 100, 2);

-- 插入几辆停车 -------------------------------car车辆表--------------------------------------------
insert into car(car_number, entry_time, departure_time)
values ('赣A123456', '2022-01-01 00:00:00', '2022-01-02 00:00:00'),
       ('赣B987654', '2022-02-01 12:00:00', '2022-02-02 11:20:00'),
       ('赣C369369', '2022-01-31 08:08:08', '2022-02-01 01:10:10'),
       ('long123456', '2021-12-01 00:00:00', '2022-5-01 00:00:00');

-- 插入2022年的收入---------------------------income收入表--------------------------------------------------
create procedure data_init_income(b int, e int)
begin
    while b <= e
        do
            insert into income(year, parkinglot_id)
            values (b, 1);
            set b = b + 1;
        end while;
end;
call data_init_income(2022, 2072);
-- 设置2022年度月收入的一些数据
update income
set annual_income = 3034,
    Jan=260,
    Feb=120,
    Mar=90,
    Apr=156,
    May=220,
    Jun=190,
    Jul=330,
    Aug=188,
    Sep=200,
    Oct=460,
    Nov=320,
    Dece=500
where year = 2022;

-- 插入几条停车记录--------------------------record停车记录表-------------------------------------------
insert into record(car_number, entry_time, departure_time, parking_time, fee)
values ('123', '2022-01-01 00:00:00', '2022-01-02 00:00:00', 24, 48),
       ('456', '2022-01-01 00:00:00', '2022-01-02 00:00:00', 24, 48),
       ('789', '2022-01-01 00:00:00', '2022-01-02 00:00:00', 24, 48);