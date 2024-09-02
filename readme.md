# Итоговая контольная работа по блоку Специализация
## 1-5. Linux
Файлы и история команд находятся в папке *linux*
## 7-13. MySQL
```
#7
create database humans_friends;
#8
create table animal (id Int NOT NULL primary key AUTO_INCREMENT, name Varchar(15));
create table home_animal (select * from animal);
create table pack_animal (select * from animal);
#9
create table cat (id Int NOT NULL primary key AUTO_INCREMENT, name Varchar(15), birth date, commands Varchar(50));
create table dog (id Int NOT NULL primary key AUTO_INCREMENT, name Varchar(15), birth date, commands Varchar(50));
create table hamster (id Int NOT NULL primary key AUTO_INCREMENT, name Varchar(15), birth date);
create table horse (id Int NOT NULL primary key AUTO_INCREMENT, name Varchar(15), birth date, commands Varchar(50));
create table camel (id Int NOT NULL primary key AUTO_INCREMENT, name Varchar(15), birth date, commands Varchar(50));
create table donkey (id Int NOT NULL primary key AUTO_INCREMENT, name Varchar(15), birth date);
INSERT into cat (name, birth, commands) VALUES ('Murzik', '2021/11/23', 'sit down, voice'), ('Murka', '2022/07/26', 'voice');
INSERT into dog (name, birth, commands) VALUES ('Pushok', '2019/08/17', 'sit down, lay, voice'), ('Sharik', '2021/03/07', 'voice, lay');
INSERT into hamster (name, birth) VALUES ('Homka', '2024/01/07'), ('Pushistik', '2023/12/27'))
INSERT into horse (name, birth, commands) VALUES ('Veterok', '2011/07/10', 'walk, run'), ('Groza', '2015/09/12', 'walk');
INSERT into camel (name, birth, commands) VALUES ('Sultan', '2010/06/24', 'walk'), ('Agata', '2012/10/06', 'walk, run');
INSERT into donkey (name, birth) VALUES ('Ia', '2012/12/10'), ('Oslo', '2012/09/13');
```
