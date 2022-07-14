def divide_five_by_number(n):
    try:
        return 5 / n
    except (ZeroDivisionError, TypeError) as e:
        return f"Something went wrong. The error was {e}"
    # except ZeroDivisionError:
    #     return 'You can\'t divide by zero!'
    # except TypeError as e:
    #     return f"No dividing by invalid objects! {e}"


print(divide_five_by_number(0))
print(divide_five_by_number(10))
print(divide_five_by_number('Nonsense'))
