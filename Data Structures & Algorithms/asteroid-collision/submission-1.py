class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        
        stack = []


        for a in asteroids:
            alive = True
            if a < 0:
                while stack and alive and stack[-1] > 0:
                    toCollide = stack.pop()
                    if abs(a) > toCollide:
                        pass
                    elif abs(a) < toCollide:
                        alive = False
                        stack.append(toCollide)
                    else:
                        alive = False
                        break
                
            if alive:
                stack.append(a)
            

        return stack

                    