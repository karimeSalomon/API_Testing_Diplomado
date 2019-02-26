Feature: withdraw fixed amount
The "Withdraw Cash" menu contains several fixed amounts to
speed up transactions for users.

    Scenario Outline: Withdraw fixed amount
        Given I have <balance> in my account
         When I choose to withdraw the fixed amount of <withdrawal>
         Then I should receive <received> cash
          And the balance of my account should be <remaining>
    Examples:
        | balance | withdrawal | received | remaining |
        |    $500 |        $50 |      $50 |      $450 |
        |    $500 |       $100 |     $100 |      $400 |
        |    $500 |       $200 |     $200 |      $300 |

