SELECT * FROM crime.crime_data;
use crime;
select Vict_Age, count(*) as crime_count from crime_data group by Vict_Age order by Crime_count desc limit 10;
select LAT, LON, count(*) as Number_of_crime from crime_data group by LAT, LON order by Number_of_crime desc;
select Vict_Sex AS GENDER, count(*) AS Crime_count, count(*) * 100.0 / sum(count(*)) OVER() AS Crime_rate_percentage from crime_data group by Vict_Sex;

select Location, count(*) as Most_Crime_no from crime_data group by Location order by Most_Crime_no desc limit 10;
select Crm_cd, count(Crm_cd) as Reported_Crime from crime_data group by Crm_Cd order by Reported_Crime desc limit 10;
select Vict_Sex, count(*) from crime_data group by Vict_Sex;