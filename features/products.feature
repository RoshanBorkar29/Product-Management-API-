Feature: Product Management

Scenario: Read a Product
  Given the following products
    | name | description | price | available | category |
    | Phone | Smart | 500 | True | Electronics |
  When I request the product "Phone"
  Then I should see the product details
  
Scenario: Update a Product
  Given the following products
    | name   | description | price | available | category     |
    | Phone  | Smart       | 500   | True      | Electronics  |
  When I update the product "Phone" with new name "Updated Phone"
  Then the product should be updated successfully
Scenario: Delete a Product
  Given the following products
    | name  | description | price | available | category    |
    | Phone | Smart       | 500   | True      | Electronics |
  When I delete the product "Phone"
  Then the product should no longer exist


Scenario: List All Products
  Given the following products
    | name  | description | price | available | category    |
    | Phone | Smart       | 500   | True      | Electronics |
    | TV    | LED         | 800   | True      | Electronics |
  When I list all products
  Then I should see all products


Scenario: Search Product by Category
  Given the following products
    | name  | description | price | available | category    |
    | Phone | Smart       | 500   | True      | Electronics |
  When I search products by category "Electronics"
  Then I should see products in "Electronics"


Scenario: Search Product by Availability
  Given the following products
    | name   | description | price | available | category    |
    | Tablet | Android     | 300   | True      | Electronics |
  When I search products by availability "True"
  Then I should see available products


Scenario: Search Product by Name
  Given the following products
    | name  | description | price | available | category    |
    | Phone | Smart       | 500   | True      | Electronics |
  When I search products by name "Phone"
  Then I should see the product "Phone"
