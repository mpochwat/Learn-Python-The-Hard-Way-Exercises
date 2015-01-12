class Parent(object):

    def override(self):
        print "PARENT override()"

    def implicit(self):
        print "PARENT implicit()"

    def altered(self):
        print "PARENT altered()"

class Child(Parent):

    def override(self):
        print "CHILD override()"

    def altered(self):
        print "CHILD, BEFORE PARENT altered()"
        super(Child, self).altered()
        print "CHILD, AFTER PARENT altered()"

dad = Parent()
son = Child()

# Implicitly uses parent's function
dad.implicit()
son.implicit()

#Uses parent function. Overrides it in son
dad.override()
son.override()

#Uses parent function. Overrides it with son. Then uses super to call parent.
# Finally returns back to son's override function.
dad.altered()
son.altered()