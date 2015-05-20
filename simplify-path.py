class Solution:
    # @param path, a string
    # @return a string
    def simplifyPath(self, path):
        stk = ['/']
        for i in path.strip('/').split('/'):
            if i == "." or i == "":
                continue
            if i == "..":
                if len(stk) > 1:
                    stk.pop()
            else:
                stk.append(i+"/")
        return "".join(stk).rstrip('/') if len(stk) > 1 else  "".join(stk)
