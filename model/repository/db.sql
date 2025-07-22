--save user
INSERT INTO USER
    (user_id,first_name,last_name,username,password,role,locked)
values
    (2,'sahel','saheli','sahelsal','sahel123','admin',1);

--find_all
select *
from USER
where user_id=2;

--edit
UPDATE USER SET first_name='sahar',last_name='summer',username='saharsum',password='sahar123',role='admin',locked=1
where user_id=1;

--delete
delete from USER where user_id=8;







