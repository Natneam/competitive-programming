class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        """
        for each email process the email user name to process the values
        track the unique email in dictionary
        
        """
        
        def process(email):
            username, domainname = email.split("@")
            t_username = username.split("+")[0]
            username = []
            for c in t_username:
                if c != ".":
                    username.append(c)
            return "".join(username) +  "@" +  domainname
        
        emails_dict = defaultdict(int)
        
        for email in emails:            
            emails_dict[process(email)] += 1
        return len(emails_dict)