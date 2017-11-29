
create table if not exists user_
(
 id int unsigned primary key auto_increment,
 name varchar(64) not null,
 password varchar(16) not null,
 mobile varchar(16),
 email varchar(64),
 avatar varchar(128),
 city varchar(32),
 hometown varchar(32),
 gender varchar(1) default '0',  /*0=male 1=female*/
 role int unsigned default 0,  /*0=普通用户 1=vip*/
 money int unsigned default 0
) engine=InnoDB, charset=utf8;

