import itertools
from Queue import Queue

class StateProblem(object):

    def __init__(self,jug_a,jug_b,goal):
        self.jug_a=jug_a
        self.jug_b=jug_b
        self.start=(0,0)
        self.end=[(goal,0),(0,goal)]
        self.transition_database={}
        state=list(itertools.product(range(jug_a+1),range(jug_b+1)))
        for data in state:
            row=[data] + self.possible_states(data,jug_a,jug_b)
            self.transition_database[row[0]]=row[1:]
        self.steps=self.prepare_steps(self.jug_a,self.jug_b)

    def prepare_steps(self,jug_a,jug_b):
        steps={ 0: "Fill the {} litre jug.".format(jug_a),
                1: "Fill the {} litre jug.".format(jug_b),
                2: "Empty the {} litre jug.".format(jug_a),
                3: "Empty the {} litre jug.".format(jug_b),
                4: "Pour water from {} litre jug into {} litre jug until {} litre jug is full.".format(jug_a,jug_b,jug_b),
                5: "Empty water from {} litre jug into {} litre jug.".format(jug_a,jug_b),
                6: "Pour water from {} litre jug into {} litre jug until {} litre jug is full.".format(jug_b,jug_a,jug_a),
                7: "Empty water from {} litre into {} litre jug.".format(jug_b,jug_a)}
        return steps

    def possible_states(self,litres,jug_a,jug_b):
        state_space=[]
        state_space.append((jug_a,litres[1]))
        state_space.append((litres[0],jug_b))
        state_space.append((0,litres[1]))
        state_space.append((litres[0],0))
        total=litres[0]+litres[1]
        if total>=jug_b:
            state_space.append((total-jug_b,jug_b))
        else:
            state_space.append('-')
        if total<jug_b:
            state_space.append((0,total))
        else:
            state_space.append('-')
        if total>=jug_a:
            state_space.append((jug_a,total-jug_a))
        else:
            state_space.append('-')
        if total<jug_a:
            state_space.append((total,0))
        else:
            state_space.append('-')
        return state_space

    def breadth_first(self):
            visited=[]
            nodes=Queue()
            visited.append(self.start)
            exit=0
            step=['Start with empty jugs.']
            result={}

            for n,i in enumerate(self.transition_database[self.start]):
                if i not in visited and type(i) is tuple:
                    visited.append(i)
                    nodes.put([(self.start),(i,n)])
                    
            while not nodes.empty():
                
                curr=nodes.get()
                if curr[-1][0] in self.end:
                    final=[]                        
                    for i in curr:
                        if i!=(0,0):
                            step.append(self.steps[i[-1]])
                    result["steps"]=step
                    for i in curr:
                        if i!=(0,0):
                            final.append(i[0])
                        else:
                            final.append((0,0))
                    result['state sequence']=final
                    break
                        
                for n,i in enumerate(self.transition_database[curr[-1][0]]):

                    if i in self.end:
                        final=[]
                        curr=curr+[(i,n)]
                        exit=1
                        
                        for i in curr:
                            if i!=(0,0):
                                step.append(self.steps[i[-1]])
                        result["steps"]=step
                        for i in curr:
                            if i!=(0,0):
                                final.append(i[0])
                            else:
                                final.append((0,0))
                        result['state sequence']=final
                        break
                    elif i not in visited and type(i) is tuple:
                        visited.append(i)
                        nodes.put(curr+[(i,n)])
                    else:
                        pass
                if exit==1:
                    break

            return result

if __name__ == '__main__':
    jug_a = int(raw_input('Enter size of container 1: '))
    jug_b = int(raw_input('Enter size of container 2: '))
    goal = int(raw_input('Enter measurement(1-%d): '%max(jug_a, jug_b)))
    if goal == 0:
        print 'Measurement cannot be zero.'
    elif goal > max(jug_a, jug_b):
        print 'Measurement cannot exceed size of largest jug.'
    else:
        Solution = StateProblem(jug_a, jug_b, goal)
        Result = Solution.breadth_first()
        if not Result:
            print 'Measurement not possible'
        else:
            for state in Result['state sequence']:
                print state,'->',
            print
            for index, step in enumerate(Result['steps']):
                print '%d.'%(index+1),step
