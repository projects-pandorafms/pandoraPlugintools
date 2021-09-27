# Python: module plugintools for PandoraFMS Developers

## Modules

* [json](json.html)  
* [os](os.html)  
* [psutil](psutil.html)  
* [sys](sys.html)  

## Classes

* [builtins.object](builtins.html#object)
* [Agent](plugintools.html#Agent)

   
class **Agent**([builtins.object](builtins.html#object))

 

Basic agent class. Requires agent parameters (config {dictionary})  
and module definition (modules\_def \[list of dictionaries\]) 

 

Methods defined here:  

**\_\_init\_\_**(self, config, modules\_def)

Initialize self.  See help(type(self)) for accurate signature.

* * *

Data descriptors defined here:  

**\_\_dict\_\_**

dictionary for instance variables (if defined)

**\_\_weakref\_\_**

list of weak references to the object (if defined)

   
## Functions

 
**auth\_call**(session, authtype, user, passw)

Authentication for url request. Requires request.sessions.Session() [object](builtins.html#object).  
   
Args:  
    session ([object](builtins.html#object)): request Session() [object](builtins.html#object).  
    authtype (str): 'ntlm', 'basic' or 'digest'.  
    user (str): auth user.  
    passw (str): auth password.

* * *

**call\_url**(url, authtype, user, passw, time\_out)

Call URL. Uses request module to get url contents.  
   
Args:  
    url (str): URL  
    authtype (str): ntlm', 'basic', 'digest'. Optional.  
    user (str): auth user. Optional.  
    passw (str): auth password. Optional.  
   
Returns:  
    str: call output
    
* * *

**debug\_dict**(func)

debug\_dict \[Decorator\]. Prints an indented json.  
Write @debug\_dict above any function that returns a dictionary or a list of dictionaries.

* * *

**now**(print\_flag=None, utimestamp=None)

Returns time in yyyy/mm/dd HH:MM:SS format by default. Use 1 as an argument  
to get epoch time (utimestamp)

* * *

**parse\_configuration**(file='/etc/pandora/pandora\_server.conf', separator=' ')

Parse configuration. Reads configuration file and stores its data as dict.
 
Args:
   + file (str): configuration file path. Defaults to "/etc/pandora/pandora\_server.conf". 
   + separator (str, optional): Separator for option and value. Defaults to " ".
 
Returns:
   + dict: containing all keys and values from file.

* * *

**print\_agent**(agent, modules, data\_dir='/var/spool/pandora/data\_in/', log\_modules=None, print\_flag=None)

Prints agent XML. Requires agent conf (dict) and modules (list) as arguments.  
+ Use print\_flag to show modules' XML in STDOUT.  
+ Returns a tuple (xml, data\_file).

* * *

**print\_log\_module**(module, print\_flag=None)

Returns log module in XML format. Accepts only {dict}.  
   
+ Only works with one module at a time: otherwise iteration is needed.  
+ Module "value" field accepts str type.  
+ Use not\_print\_flag to avoid printing the XML (only populates variables).

* * *

**print\_module**(module, print\_flag=None)

Returns module in XML format. Accepts only {dict}.  
   
+ Only works with one module at a time: otherwise iteration is needed.  
+ Module "value" field accepts str type or \[list\] for datalists.  
+ Use print\_flag to show modules' XML in STDOUT.

* * *

**tentacle\_xml**(file, tentacle\_ops, tentacle\_path='', debug=0)

Sends file using tentacle protocol  
   
+ Only works with one file at time.  
+ file variable needs full file path.  
+ tentacle\_opts should be a dict with tentacle options (address \[password\] \[port\]).  
+ tentacle\_path allows to define a custom path for tentacle client in case is not in sys path).  
+ if debug is enabled, the data file will not be removed after being sent.  
   
Returns 0 for OK and 1 for errors.

* * *

**write\_xml**(xml, agent\_name, data\_dir='/var/spool/pandora/data\_in/')

