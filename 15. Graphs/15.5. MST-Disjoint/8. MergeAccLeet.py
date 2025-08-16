class Solution:
    def dfs(self, node, graph, visited, component):
        if visited[node]:
            return
        visited[node] = True
        component.append(node)
        for neighbor in graph[node]:
            if not visited[neighbor]:
                self.dfs(neighbor, graph, visited, component)

    def accountsMerge(self, accounts):
        graph = {}
        visited = {}
        email_to_account = {}

        for account in accounts:
            emails = account[1:]
            first_email = emails[0]
            for email in emails:
                graph.setdefault(email, set()).add(first_email)
                graph.setdefault(first_email, set()).add(email)
                visited[email] = False
                email_to_account[email] = account[0]

        output = []
        for email, account in email_to_account.items():
            if visited[email]:
                continue
            nodes = []
            self.dfs(email, graph, visited, nodes)
            output.append([account] + sorted(nodes))

        return output

# Link: https://leetcode.com/problems/accounts-merge/
