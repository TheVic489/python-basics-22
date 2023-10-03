create or replace PROCEDURE proc_bonus_vpc
IS
CURSOR salary_bonus_cur IS
SELECT salary, bonus 
FROM EMPLOYEES_EXAM;

BEGIN
for sal_bon_rec in cur_employees loop
  case 
    when salary <= 8000 then
      update EMPLOYEES_EXAM
        set bonus = 1000;
    when salary > 8000 then
      update EMPLOYEES_EXAM
        set bonus = salary * 0,125;
  end case;
end loop 
    
END proc_bonus_vpc;
