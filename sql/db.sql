
create table if not exists dc_user
(
 id int unsigned primary key auto_increment,
 name varchar(64) not null,
 password varchar(512) not null,
 mobile varchar(16),
 telephone varchar(16),
 email varchar(256),
 avatar varchar(512),
 city varchar(32) not null,
 department varchar(64) not null, /*部门*/
 place varchar(128),           /*职称级别*/
 gender int unsigned default 0,  /*0=male 1=female*/
 role int unsigned default 0   /*0=查询用户 1=信息联络员 2=业务维护员*/
) engine=InnoDB, charset=utf8;

insert into dc_user(id, name, password, city, department, place, gender, role) values(1, 'admin', '123', '成都', '货币信贷统计处', '处长', 1, 2);
insert into dc_user(id, name, password, city, department, place, gender, role) values(2, 'tq', '123', '成都', '稳定处', '一般干部', 0, 1);

/*部门表*/
create table if not exists department
(
 id int unsigned primary key auto_increment,
 name varchar(128) not null /*部门的名字*/
) engine=InnoDB, charset=utf8;

insert into department(id, name) values(1, '货币信贷统计处');
insert into department(id, name) values(2, '调统处');
insert into department(id, name) values(3, '稳定处');
insert into department(id, name) values(4, '征信处');
/*职务表*/
create table if not exists position_
(
 id int unsigned primary key auto_increment,
 name varchar(128) not null /*职称名字*/
) engine=InnoDB, charset=utf8;

insert into position_(id, name) values(1, '行级干部');
insert into position_(id, name) values(2, '处级干部');
insert into position_(id, name) values(3, '科级干部');
insert into position_(id, name) values(4, '一般干部');

/*城市表*/
create table if not exists city
(
 id int unsigned primary key auto_increment,
 name varchar(128) not null /*城市名字*/
) engine=InnoDB, charset=utf8;

insert into city(id, name) values(1, '广州');
insert into city(id, name) values(2, '厦门');
insert into city(id, name) values(3, '杭州');
insert into city(id, name) values(4, '哈尔滨');
insert into city(id, name) values(5, '长春');
insert into city(id, name) values(6, '大连');
insert into city(id, name) values(7, '青岛');
insert into city(id, name) values(8, '宁波');
insert into city(id, name) values(9, '沈阳');
insert into city(id, name) values(10, '济南');
insert into city(id, name) values(11, '南京');
insert into city(id, name) values(12, '武汉');
insert into city(id, name) values(13, '西安');
insert into city(id, name) values(14, '成都');

create table if not exists auth
(
 id int unsigned primary key auto_increment,
 name varchar(32) not null,
 tag int unsigned default 0
) engine=InnoDB, charset=utf8;
