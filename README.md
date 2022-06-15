# usl_bs_employee_management


This is done in `odoo 13`

Add this module to your running odoo project

Then update the odoo app list and install `bs_odoo_writen_test`

I've added a sub menu to Sales -> Orders -> Employee Info

There are User group in user settings named `Employee Setup Group`

Select `HR Manager` for creating new Employee

As odoo 13 has not department concept for that reason I can't add rule for department wise B.Access Control

Here is the code for department wise rule
```    
  <data noupdate="1">
        <record id="ir_rule_set_department_wise_employee" model="ir.rule">
            <field name="name">Department Wise Employee List</field>
            <field name="model_id" ref="bs_odoo_writen_test.model_employee_info"/>
            <field name="domain_force">[('department', '=', user.department)]</field>
            <field name="groups" eval="[(4, ref('bs_odoo_writen_test.group_employee_management_dep_manager'))]"/>
        </record>
    </data>
    
