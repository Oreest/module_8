contacts = dict()

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return 'Wrong name'
        except TypeError:
            return 'Please enter correct command'
        except IndexError:
            return 'Wrong amount values'
        except ValueError:
            return "Give me Name and Phone Number, please"

    return inner
@input_error
def add(data: list):
    if data[0] in contacts:
        raise KeyError
    if not (data[1]).isnumeric():
        raise ValueError
    contacts.update({data[0]: data[1]})
    print(f'Added new Contact "{data[0]}"')

@input_error
def change(data):
    if not (data[1]).isnumeric():
        raise ValueError
    contacts[data[0]] = data[1]
    print(f'Number for "{data[0]}" has been changed!')
@input_error
def find_phone(name):
    return (f'Number: {contacts[name[0]]}')

#def help_command():
@input_error
def show_all():
    for name, number in contacts.items():
        print(f'Contact: "{name}"  Number: {number}')
        continue

@input_error
def hello():
    return 'Hello, How can I help you?'
@input_error
def wrong_command():
    return 'Wrong command.. Make sure you typed correctly and try again.'


COMMANDS = {
    'hello': hello,
    'add': add,
    'change': change,
    'phone': find_phone,
    'show all': show_all,
    'wrong command': wrong_command
}
@input_error
def handler(user_line):
    result = {
        'user_command': '',
        'data': []
    }
    if user_line.lower() == 'show all':
        result['user_command'] = user_line.lower()
        #print(result)
        return result['user_command'], result['data']
    user_line_list = user_line.split(' ')
    #print(user_line_list)
    result['user_command'] = user_line_list[0].lower()
    result['data'] = user_line_list[1:]

    return result['user_command'], result['data']
@input_error
def command_handler(command):
    if command not in COMMANDS:
        return COMMANDS['wrong command']
    return COMMANDS[command]
def main():
    while True:
        user_input = input(">>")
        if user_input.lower() == 'exit' or user_input.lower() == 'good bye' or user_input.lower() == 'bye':
           print("Good bye")
           break
        command, data = handler(user_input)
        #print(command, data)
        if not data:
            result = command_handler(command)
            result()
            continue
        result = command_handler(command)(data)
        print(type(result))
        print(result)
        #print(command, data)


if __name__ == "__main__":
    print("Welcome to CLI contacts bot.")
    print("Please enter your command\n ")
    main()