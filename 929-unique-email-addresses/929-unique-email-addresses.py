class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        #need to clean the emails/remove unnecessary characters, onces it is c          cleaned it can be stored in hashset
        
        #skip all periods
        #skip everything in betweeen + and @ sign
        
        #hashset to store unique emails
        uniqueEmails = set()
        
        for email in emails:
            
            clean = []
            
            for currChar in email:
                
                if currChar == "+" or currChar == "@":
                    #break until @ sing
                    break
                if currChar != ".":
                    clean.append(currChar)
                    
            address = []
            for currChar in reversed(email):
                if currChar != "@":
                    address.append(currChar)
                if currChar == "@":
                    break;
            
            cleanJoined = "".join(clean)
            addressJoined = "".join(address)
            cleanJoined +=addressJoined
            
            uniqueEmails.add(cleanJoined)
        return len(uniqueEmails)
            
            