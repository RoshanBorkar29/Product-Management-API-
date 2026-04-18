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
