from padatious import IntentContainer

container = IntentContainer('intent_cache')
container.add_intent('greetings', ['Hi there!', 'Hello.'])
container.add_intent('goodbye', ['See you!', 'Goodbye!'])
container.add_intent('search', ['Search for {query} (using|on) {engine}.'])
container.train()

print(container.calc_intent('Hi!'))
print(container.calc_intent('Search for cats on CatTube.'))

result=container.calc_intent('search mamamamam')
print(result.name)


if __name__ == '__main__':

 if (result.name=="search"):
     print("you are searching")
 elif (result.name=="greetings"):
     print("ami greet")
 else:
     print("ami kisui na")




