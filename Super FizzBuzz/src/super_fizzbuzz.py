def super_fizzbuzz(number):
    result = ""
    if number % 3 == 0 :
        result.append('Fizz')
        if number % 9 == 0:
            result.append('Fizz')
            if number % 25 == 0:
                result.append('BuzzBuzz')
        elif number % 5 == 0:
            result.append('Buzz')
    elif number % 5 == 0 :
        result.append('Buzz')
        if number % 25 == 0:
            result.append('Buzz')
    else:
        result = ['NoFizzBuzz']
    
    return str(result)