create database if not exists ParkingSys;
use ParkingSys;
-- 停车场表
create table if not exists Parkinglot
(
    parkinglot_id    int auto_increment primary key comment '停车场编号',
    address          varchar(20) not null comment '地址',
    total_space      int         not null comment '总车位',
    remain_space     int         not null comment '剩余车位',
    charing_standard double      not null comment '收费标准',
    check ( remain_space >= 0 )
);

-- 车辆表
create table if not exists Car
(
    car_number     varchar(20) primary key comment '车牌号',
    entry_time     datetime comment '驶入时间',
    departure_time datetime comment '驶出时间'
);

-- 停车记录表
create table if not exists Record
(
    id             int auto_increment primary key comment '记录ID',
    car_number     varchar(20) comment '车牌号(不能在这做主键)',
    entry_time     datetime comment '驶入时间',
    departure_time datetime comment '驶出时间',
    parking_time   int comment '停车时长',
    fee            double comment '停车费'
);

-- 收入表
create table if not exists Income
(
    year          int primary key comment '年度',
    parkinglot_id int comment '停车场编号(外键)',
    annual_income double default 0 comment '年收入',
    Jan           double default 0 comment '一月收入',
    Feb           double default 0 comment '二月收入',
    Mar           double default 0 comment '三月收入',
    Apr           double default 0 comment '四月收入',
    May           double default 0 comment '五月收入',
    Jun           double default 0 comment '六月收入',
    Jul           double default 0 comment '七月收入',
    Aug           double default 0 comment '八月收入',
    Sep           double default 0 comment '九月收入',
    Oct           double default 0 comment '十月收入',
    Nov           double default 0 comment '十一月收入',
    Dece          double default 0 comment '十二月收入',
    constraint foreign key (parkinglot_id) references Parkinglot (parkinglot_id)
);


-- 触发器 车辆进入,剩余车位-1

create trigger insert_car
    after insert
    on car
    for each row
begin
    update parkinglot
    set remain_space = remain_space - 1
    where parkinglot_id = 1;
end;

-- 触发器 车辆驶出,剩余车位+1,并插入记录到停车记录表

create trigger delete_car
    before delete
    on car
    for each row
begin
    declare number varchar(20);
    declare etime datetime;
    declare dtime datetime;
    declare ptime_h int;
    declare ptime_m int;
    declare standard double;
    set number = OLD.car_number;
    set etime = OLD.entry_time;
    set dtime = OLD.departure_time;
    set ptime_m = timestampdiff(minute, etime, dtime);
    set ptime_h = timestampdiff(hour, etime, dtime);
    # 超半小时但不满一小时按一小时计算
    if ptime_m / 60.0 >= ptime_h + 0.5 then
        set ptime_h = ptime_h + 1;
    end if;
    set standard = (select charing_standard from parkinglot where parkinglot_id = 1);
    # 插入记录到Record
    insert into record(car_number, entry_time, departure_time, parking_time, fee)
    values (number, etime, dtime, ptime_h, ptime_h * standard);
    # 停车场剩余车位+1
    update parkinglot
    set remain_space = remain_space + 1
    where parkinglot_id = 1;
end;

-- 触发器 停车记录插入，计算收入增加到收入表中

create trigger insert_record
    after insert
    on record
    for each row
begin
    declare increa double;
    declare mon int;
    declare year_ int;
    set increa = NEW.fee;
    set mon = (select month(curdate()));
    set year_ = (select year(curdate()));
    update income
    set annual_income = annual_income + increa where year = year_;
    if
        mon = 1 then
        update income set Jan = Jan + increa where year = year_;
    elseif
        mon = 2 then
        update income set Feb = Feb + increa where year = year_;
    elseif
        mon = 3 then
        update income set Mar = Mar + increa where year = year_;
    elseif
        mon = 4 then
        update income set Apr = Apr + increa where year = year_;
    elseif
        mon = 5 then
        update income set May = May + increa where year = year_;
    elseif
        mon = 6 then
        update income set Jun = Jun + increa where year = year_;
    elseif
        mon = 7 then
        update income set Jul = Jul + increa where year = year_;
    elseif
        mon = 8 then
        update income set Aug = Aug + increa where year = year_;
    elseif
        mon = 9 then
        update income set Sep = Sep + increa where year = year_;
    elseif
        mon = 10 then
        update income set Oct = Oct + increa where year = year_;
    elseif
        mon = 11 then
        update income set Nov = Nov + increa where year = year_;
    elseif
        mon = 12 then
        update income set Dece = Dece + increa where year = year_;
    end if;
end;

