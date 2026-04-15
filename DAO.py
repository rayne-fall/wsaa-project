# DAO
# author: Sylvia Chapman Kent
# interacts with a database containing details of various examples of media
import mysql.connector
import config as cfg

class MediaDAO:
    connection=""
    cursor =''
    host=       ''
    user=       ''
    password=   ''
    database=   ''
    
    # initialise
    def __init__(self):
        self.host=       cfg.mysql['host_cred']
        self.user=       cfg.mysql['user_cred']
        self.password=   cfg.mysql['pass_cred']
        self.database=   cfg.mysql['db']
    # get the cursor
    def getcursor(self): 
        self.connection = mysql.connector.connect(
            host=       self.host,
            user=       self.user,
            password=   self.password,
            database=   self.database,
        )
        self.cursor = self.connection.cursor()
        return self.cursor
    # close the cursor
    def closeAll(self):
        self.connection.close()
        self.cursor.close
    # display all entries in the table of tv shows
    def getAlltv(self):
        cursor = self.getcursor()
        sql="select * from tv_shows"
        cursor.execute(sql)
        results = cursor.fetchall()
        returnArray = []
        #print(results)
        for result in results:
            #print(result)
            returnArray.append(self.convertToDictionary(result))
        self.closeAll()
        return returnArray
    # search the table for an id and display that tv show
    def findTVByID(self, id):
        cursor = self.getcursor()
        sql="select * from tv_shows where id = %s"
        values = (id,)

        cursor.execute(sql, values)
        result = cursor.fetchone()
        returnvalue = self.convertToDictionary(result)
        self.closeAll()
        return returnvalue
    
    # convert the details and their columns to a dictionary object
    def convertToDictionary(self, resultLine):
        attkeys=['id','title','genre', "year"]
        tv_show = {}
        currentkey = 0
        for attrib in resultLine:
            tv_show[attkeys[currentkey]] = attrib
            currentkey = currentkey + 1 
        return tv_show
    
mediaDAO=MediaDAO