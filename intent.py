from padatious import IntentContainer


def parseMsg(msg):
    container = IntentContainer('intent_cache')

    container.add_intent('greetings',
                         ['hi.', 'hellow', '(waz|wazz|wad) up?', 'hey', 'yoo', 'buddy', '(you|hey) there?'])
    container.add_intent('bye', ['bye.', 'tata', 'thank you', 'adios', 'thanks', 'allah hafez', 'done'])
    # container.add_intent('goal', ['i want to go (|to) {goal}', '(destination|i wanna go) {goal}',
    #                               'destination is {goal}'])
    # container.add_intent('start', ['from {start}', '(i am (in|at){start}'
    #                                ])
    container.add_intent('search',
                         ['I want to go from {start} to {goal}.', 'I want to (go to|go) {goal} from {start}.'])
    container.add_intent('ajaira', ['lala', 'kchdskfhsk', 'iwurhb', 'uerwyvdsvjjkc', 'sufgbsdjc'])

    container.train()
    result = container.calc_intent(msg)
    print(result)
    print(result.name)
    # print(str(result.matches['start']))
    # print(result.matches['start'])
    # print(result.matches['goal'])
    return result


# parseMsg("i want to go  khilgaon")
# work with the full result
