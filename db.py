# -*- coding: utf-8 -*-
import sqlite3
DATABASE = "predict.db"

class Database:
    def __init__(self, db):
        self.con = sqlite3.connect(db)
        self.cur = self.con.cursor()
        # self.cur.execute("DROP TABLE IF EXISTS predict")
        # self.cur.execute("DROP TABLE IF EXISTS predict_details")
        # self.cur.execute("DROP TABLE IF EXISTS type")

        self.cur.execute("CREATE TABLE IF NOT EXISTS predict(id INTEGER PRIMARY KEY, code INTEGER, type_code INTEGER, description TEXT)")
        # self.cur.execute("CREATE TABLE IF NOT EXISTS type(type_code INTEGER PRIMARY KEY, type_detail)")
        # self.cur.execute("CREATE TABLE IF NOT EXISTS predict_details(id INTEGER PRIMARY KEY, code INTEGER, predict_detail_id INTEGER REFERENCES predict_details(id), type_code INTEGER REFERENCES type(type_code))")
        self.con.commit()

    def fetch(self, sql):
        self.cur.execute(sql)
        rows = self.cur.fetchall()
        return rows

    def executeUpdate(self, sql, data):
        self.cur.execute(sql, data)
        self.con.commit()

    def executeQuery(self, sql, data):
        self.cur.execute(sql, data)
        return self.cur.fetchall()
        

    def __del__(self):
        self.con.close()


class Predict:
    def __init__(self):
        self.db = Database(DATABASE)
    
    def fetchAll(self):
        return self.db.fetch(sql="SELECT * FROM predict")
    
    def insert(self, id, code, type_code, description):
        return self.db.executeUpdate("INSERT INTO predict(id, code, type_code, description) VALUES (?, ?, ?, ?)", (id, code, type_code, description))

    def getPredictByCode(self, code):
        return self.db.executeQuery("SELECT * FROM predict WHERE code = ?", (str(code)))


pd = Predict()
# pd.insert(1, 1, 1, "សម្បូរដោយសេចក្ដីក្លាហាន និង គំនិតផ្សងព្រេងគំនិតអារកាត់ខ្លាំងឯកច្ឆន្ទ ។ ជាទូទៅច្រើនប្រកបដោយការឆ្មើងឆ្មៃយ៉ាងមាំទាំ និង ថាមពលខាងចរិយាដ៏ធំចំពោះសត្រូវ ។ ជាមនុស្សកើតមកសម្រាប់ធ្វើជាមេគេ ឬក៏ជាអ្នកល្បីល្បាញបើប្រសិនជាគ្មានកាលៈទេសៈអ្វីមកខ្ទាស់ការរីកចំរើនខាងផ្លូវគំនិ")
# pd.insert(2, 1, 2, "ជាមនុស្សមានគំនិតថ្លៃថ្នូរ ហើយខ្ពង់ខ្ពស់ព្រមទាំងប្រកបដោយប្រាជ្ញាឈ្លាសវៃ ប្លែកពីគេ ។ ជាអ្នកតែងធ្វើឱ្យគេចាប់អារម្មណ៍មកលើខ្លួនហើយច្រើនកាន់កាប់ មុខងារធំដុំនៅកន្លែងធ្វើការ ។ ដោយហេតុជនជំពូកលេខ១នេះមានបុគ្គលភាព ត្រចះត្រចង់ជននេះក៏ក្លាយជាអ្នកមានវាសនាខាងធ្វើអោយមានអ្ន")
# pd.insert(3, 1, 3, "ជនជំពូកលេខ ១មានទំនោរចិត្ដជាអ្នកត្រួតត្រាហើយចូលចិត្ដបញ្ជាលើមនុស្ស ដែលខ្លួនជ្រើសរើសជាគូគាប់ណាស់ ។ ច្រើនមានចិត្ដប្រច័ណ្ឌមិនព្រមឱ្យគូគាប់ របស់ខ្លួនមានចិត្ដវៀចវេរទេ ។ បើរៀបការជាមួយមនុស្សជំពូកលេខ២ និង លេខ៦ទើបល្អ ។ មិនសូវល្អជាមួយនឹង៥ ឬលេខ៧ ព្រោះច្រើនទាស់ទែងគ្នា")
# pd.insert(4, 1, 4, "ជាមនុស្សដែលកើតមកសម្រាប់តែបានទទួលជោគជ័យក្នុងអ្វីៗដែលខ្លួនកាន់កាប់ ។ ថ្វីបើគេជាអ្នកមានគំនិតខាងការបង្កើត ហើយពិចារណាច្រើនក្ដី មនុស្ស ជំពូកលេខ១ ធ្វើការក្នុងរដ្ឋបាលក៏ពូកែ រត់ការក៏ពូកែ ។ តែទោះជាធ្វើការអ្វីក៏ ដោយមនុស្សនេះត្រូវកាន់កាប់ការនោះតែម្នាក់ឯង ឬធ្វើជាមេគេទ")
# pd.insert(5, 1, 5, "មនុស្សជំពូកលេខ១ប្រសប់ប្រកបរបរណាស់ហើយតែងរកចំណេញបានច្រើនផង ។ តែជាអកុសលរកបានប៉ុន្មាន ចាយអស់ប៉ុណ្ណឹង បើនិយាយឱ្យខ្លី គឺរកក៏ធូរ ចាយក៏ធូរ ។")
# pd.insert(6, 2, 1, "មានចរិតជាអ្នកឆាប់រំភើបបំផុតឆាប់ខឹង តែចូលចិត្ដគោរព អ្នកដទៃ ។ ជាអ្នកចេះស្ដាប់បង្គាប់ ចូលចិត្ដឱ្យគេដឹកនាំជាជាងបញ្ជាគេ ។ មនុស្សជំពូកនេះ ពេញចិត្ដនឹងការរាក់ទាក់រាប់អានណាស់ ហើយតែងតែខិតខំ បំពេញបំណងជនដែលមកសុំជំនួយពីខ្លួន ។")
# pd.insert(7, 2, 2, "ដោយខ្លួនជាអ្នករាក់ទាក់មនោសញ្ចេតនាចូលចិត្ដនិយាយរឿងផ្ទាល់ខ្លួនប្រាប់គេមនុស្សជំពូកលេខ២ តែងបណ្ដោយខ្លួនទៅតាមទឹកចិត្ដ ជាជាងទៅតាម វិចារណញ្ញាណ នៅពេលខ្លួនក្ដាប់ស្ថានការណ៍បានហើយក្ដី ក៏មនុស្សជំពូក លេខ២តែងតែនៅមានការរំភើបជានិច្ចនៅពេលដែលខ្លួនជួបប្រទះនឹងការ លំបាក ។ ដោយខ")
# pd.insert(8, 2, 3, "មនុស្សជំពូកលេខ២ច្រើនជាស្វាមីឬភរិយាគ្រប់លក្ខណ៍ ។ ការពិតមនុស្ស ជំពូក នេះដោយអាស្រ័យលើទឹកចិត្ដសណ្ដោសនិងមនោសញ្ចេតនារបស់ខ្លួនតែងប្រឹង ប្រែងផ្ដល់ឱ្យគូគាប់របស់ខ្លួននូវសុខុមាលភាពនិងសុភមង្គល ។ មានពេលខ្លះទោះ ជានៅចំពោះមុខសីលធម៌ឬក៏ប្រាកដនិយមដែលជាការចាំបាច់សម្រាប់ការរស")
# pd.insert(9, 2, 4, "ជាមនុស្សគិតច្រើននិងមានគំនិតបង្កើតតែកង្វះខាងភាពឈ្លានពានរបស់មនុស្សនេះ តែងនាំឱ្យមនុស្សជំពូកនេះចូលចិត្ដធ្វើជាចិត្ដវិទូជាឧបការីសង្គមនិងជា លេខាធិការដ៏មានប្រសិទ្ធភាព ។ សរុបសេចក្ដីទៅគឺជាមនុស្សដែលកើតមក សម្រាប់តែទទួលជោគជ័យក្នុងវិជ្ជាជីវៈណាដែលតម្រូវឱ្យមានមនសិការវិជ្")
# pd.insert(10, 2, 5, "ជាអ្នកសន្សំប្រាក់ផុតលេខហើយមិនចូលចិត្ដខាតបង់លុយកាក់ទទេៗក្នុងមុខរបរមានគ្រោះថ្នាក់ឬមិនជាក់ច្បាស់ឡើយ ។ គឺចូលចិត្ដយកលុយទៅរកស៊ីដោយមាន បែបផែន ហើយមិនចូលចិត្ដលេងល្បែងស៊ីសងទេ ។ ប៉ុន្ដែដោយខ្លួនជាអ្នកចិត្ដល្អពីធម្មជាតិមកនោះមនុស្សជំពូកនេះហ៊ានចំណាយទៅលើមនុស្សដែលខ្លួនស្រ")
# pd.insert(11, 3, 1, "ជាមនុស្សពោរពេញដោយថាមពលនិងគំនិតបង្កើតស្រឡាញ់ជីវភាពតាមគ្រប់លក្ខណៈហើយអ្វីក៏អាចទាក់ចិត្ដគេបានដែរ ។ ជាអ្នកសុទិដ្ឋិនិយម និង ទុកចិត្ដខ្លួនឯង ។ ចេះភ្លក់រសជាតិនៃការសប្បាយនៃជីវិតហើយចេះទទួលទិដ្ឋិភាពជា វិជ្ជមានក៏ដូចជាទិដ្ឋិភាពមិនសូវសប្បាយដែរ ។ រហ័សរហួន ហើយឆាប់ទទួល ឥទ")
# pd.insert(12, 3, 2, "ចូលចំណោមឆាប់ចុះរហូតដល់គេអាចនិយាយបានថាមនុស្សជំពូកលេខ៣នេះគឺជាមនុស្សងាយសម្របតាមជីវភាពក្នុងសហគមន៍បំផុត ។ ជាអ្នកចេះទប់ចិត្ដបានយ៉ាងត្រចះត្រចង់ហើយយ៉ាងសប្បាយទៀតរួចចេះធ្វើឱ្យអ្នកផងពេញចិត្ដគ្រប់ៗគ្នា ។ អ៊ីចឹងហើយបានជាមនុស្សនេះងាយរកមិត្ដភាពពី អ្នកដទៃណាស់ ។ បានជាឆាប់ទ")
# pd.insert(13, 3, 3, "ថ្វីបើមនុស្សជំពូកលេខ៣ជាអ្នកមានទឹកចិត្ដទោរទន់ក៏ដោយក៏នៅមុនពេលរកគូស្រករមនុស្សនេះចូលចិត្ដធ្វើពិសោធន៍ចិត្ដគូគាប់របស់ខ្លួនមុនជានិច្ច ។ លុះរៀបការហើយមនុស្សនេះតែងខិតខំបំពេញចិត្ដគូគាប់និងកូនចៅរបស់ខ្លួនណាស់ ។ យកល្អត្រូវរៀបការនឹងមនុស្សជំពូកលេខ៣ដូចគ្នា និងលេខ៨ ។")
# pd.insert(14, 3, 4, "ដោយមានការរហ័សរហួន និងគំនិតផ្ដើមពីធម្មជាតិមកស្រាប់មនុស្សនេះចូលចិត្ដ ប្រកបរបរណាដែលខ្លួនអាចបង្ហាញឱ្យឃើញនូវការប៉ិនប្រសប់ និងគំនិតផ្ដួចផ្ដើម របស់ខ្លួនណាស់ ។ បើធ្វើជាអ្នកកាសែតអ្នកថតរូបវិចិត្រករ គឺប្រសើរណាស់ ព្រោះអាចបានទទួលជោគជ័យច្រើន ។ ម្យ៉ាងទៀតមុខរបរខាងការផ្សា")
# pd.insert(15, 3, 5,"ជាមនុស្សចិត្ដល្អហើយចាយធំផង ។ ចូលចិត្ដធ្វើម៉េចឱ្យតែអ្នកមកជួបនឹងខ្លួនបានសប្បាយចង់អស់ប៉ុន្មានក៏អស់ទៅ ព្រោះចូលចិត្ដគិតថា លុយមិនមែនធ្វើមកសម្រាប់តែសន្សំ តែសម្រាប់ចាយ ឱ្យបានសប្បាយចិត្ដ ។")
# pd.insert(16, 4, 1, "ជាអ្នកធ្វើការមិនខ្លាចនឿយហត់ប្រកបដោយគំនិតម៉ឺងម៉ាត់និងប្រាកដនិយម ។ មនុស្សជំពូកលេខ៤ស្រឡាញ់វិជ្ជាជីវៈរបស់ខ្លួនណាស់ ។ ជាទូទៅ ដោយអាស្រ័យលើគុណសម្បត្ដិពិសេសរបស់ខ្លួនជាអ្នករៀបចំ និងដឹកនាំ មនុស្សនេះ ច្រើនទទួលជោគជ័យជានិច្ចក្នុងកិច្ចការ ។ គុណសម្បត្ដិពិសេសរបស់មនុស្សជំ")
# pd.insert(17, 4, 2, "ជាអ្នកប្រយ័ត្នប្រយែង ហើយគត់មត់ ។ មិនងាយប្រព្រឹត្ដអំពើផ្ដេសផ្ដាសទេ ព្រោះជាមនុស្សមានស្មារតីម៉ឺម៉ាត់ មិនចេះរវើរវាយ ។ គឺជាមិត្ដភក្ដិដ៏ប្រសើរ ខាងស្មោះត្រង់បំផុតតែមិនពូកែខាងប្រើទឹកមុខទេហើយឆាប់ខឹងណាស់ ។ បើនឹងជឿលើរឿងអ្វីមួយគឺទាល់តែពិចារណាហ្មត់ចត់ណាស់តែបើទុកចិត្ដហ")
# pd.insert(18, 4, 3, "មនុស្សជំពូកលេខ៤ មិនងាយចាប់ចិត្ដស្រឡាញ់គេងាយៗទេ ហើយបើនឹងរៀបការជាមួយអ្នកណាម្នាក់វិញ ទាល់តែបានសង្កេតមើលចិត្ដថ្លើមអស់ចិត្ដអស់ចង់ ។ គឺជាភរិយាឬស្វាមីដ៏ប្រសើរប្រកបដោយគំនិតទទួលខុសត្រូវ និងសីលធម៌ ។ និយាយឱ្យខ្លីទៅបើលោកអ្នកចង់រកគូស្រករជាអ្នករវើរវាយហើយល្ងង់ខ្លៅសូមកុំ")
# pd.insert(19, 4, 4, "ដោយមានធម្មជាតិជាអ្នកស្រឡាញ់ការសិក្សាមនុស្សជំពូកលេខ៤មាននិស្ស័យ ខាងកិច្ចការណាដែលមានទ្រឹស្ដី ជាអាទ៍ ។ គេច្រើនជាគណិតវិទូអ្នកស្រាវជ្រាវ វិស្វករ និងសាស្ដ្រាចារ្យ ។ ជាទូទៅមុខរបររបស់គេមិនហុចជោគជ័យឱ្យឃើញ ភ្លាមៗទេ ។ តែបើនឹងចាប់កិច្ចការអ្វីមួយហើយអ្នកដែលស្គាល់គេតែងសរ")
# pd.insert(20, 4, 5, "មនុស្សជំពូកលេខ៤ប្រើលុយកាក់ដោយប្រយ័ត្នប្រយែងណាស់ហើយមិនស្រប រកស៊ីក្នុងមុខរបរណាដែលអាចមានកំហាតបង់ទេ ។ គេចូលចិត្ដសន្សំលុយហើយពូកែទុកដាក់បំផុត ។ ស្ថានភាពហិរញ្ញវត្ថុរបស់គេ ច្រើនតែមាំទាំ ។ គេមិនមែនជាមនុស្សកំណាញ់ទេតែបើនឹងចាយវាយគឺគេចាយ តែលុយណាដែលគេយល់ថាអាចចាយបាន ។")
# pd.insert(21, 5, 1, "មានទំនោរចិត្ដជាអ្នកស្វាហាប់រហ័សរហួនប្រកបដោយ ថាមពល ។ ដោយមានគំនិតផ្សងព្រេងជានិស្ស័យមនុស្សនេះស្រឡាញ់សេរីភាពណាស់ហើយដើម្បីសេរីភាពមនុស្សនេះមិនញញើតនឹងលះបង់អ្វីៗគ្រប់យ៉ាង ។ គ្មានអ្វីដែលថាធ្វើទៅមិនកើតសម្រាប់មនុស្សនេះទេហើយការណាដែលគេថា មិនអាចធ្វើបាន មនុស្សនេះចូលចិត្")
# pd.insert(22, 5, 2, "ហ៊ានអារកាត់ដោយឥតរារែក គឺគេជាមនុស្សក្នុងជំពូកអ្នកដែលហ៊ានសំរេច កិច្ចការ ដោយមិនសូវគិតច្រើន ។ គេជាអ្នកប្រកបដោយគំនិតភ្លឺស្វាង និង គួរឱ្យទាក់ចិត្ដនៅក្នុងសង្គម ។ បើនិយាយឱ្យសាមញ្ញគឺស៊ីដាច់គេដាច់ឯងតែម្ដង មិត្ដភក្ដិក៏ច្រើនអ្នកសើចសរសើរក៏ច្រើនទៀត ។ ក៏ប៉ុន្ដែជនជំពូកលេ")
# pd.insert(23, 5, 3, "ដោយគេជាអ្នកឆ្លាតឆ្លុំក្នុងរឿងស្នេហាគេច្រើនបានទទួលជោគជ័យជានិច្ច ។ គេចូលចិត្ដរៀបការយ៉ាងហ៊ឹកហ៊ាក់ហើយការរស់នៅជាមួយគេច្រើនតែបានជួប ប្រទះនឹងរឿងថ្មីជានិច្ចតែរឿងថ្មីទាំងនេះមិនមែនសុទ្ធតែជារឿងសប្បាយទេ ។ គេត្រូវរៀបការជាមួយមនុស្សជំពូកលេខ៥ដូចគ្នាហើយការរួមរស់របស់គេច្រើ")
# pd.insert(24, 5, 4, "អ្វីៗដែលធ្វើឱ្យមនុស្សបានទទួលជោគជ័យភ្លាមៗដូចជាការប៉ិនប្រសប់ការឈ្លាសវៃនិងការវាយឫកគឺសុទ្ធតែលក្ខណៈរបស់មនុស្សជំពូកលេខ៥ទាំងអស់ ។ ក៏ប៉ុន្ដែ ដោយហេតុថាមនុស្សជំពូកនេះច្រើនជាអ្នករហេចរហាច ខ្វះវិន័យមនុស្សនេះ ច្រើនទទួលជោគជ័យក្នុងមុខរបរណាដែលអាចឱ្យខ្លួនគេសំដែងអំណោយធម្មជា")
# pd.insert(25, 5, 5, "ចំពោះរឿងលុយកាក់ មនុស្សនេះច្រើនជួបឧបសគ្គ ។ ជួនកាលគេជាមហាសេដ្ឋី ជួនកាលគេក៏ក្ររហាមដែរ ។ ការពិតគេជាអ្នកចាយធំហើយចូលចិត្ដបំពេញចំណូលចិត្ដរបស់ខ្លួនគ្រប់យ៉ាង ដោយគ្មានខ្វល់ថារឿងសប្បាយនោះនឹងឱ្យខ្លួនគេទៅរួចឬក៏ទេឡើយ ។ មនុស្សជំពូកនេះឥតចេះសន្សំលុយកាក់ទាល់តែសោះហើយរឿងរត់ក")
# pd.insert(26, 6, 1, "ជាអ្នកប្រកបដោយអាត្ម័នថ្លៃថ្នូរហើយសុចរិត ។ គេសំគាល់មនុស្សនេះបានត្រង់មាននិស្ស័យខាងស្រឡាញ់យុត្ដិធម៌និងកាតព្វកិច្ច ។ គេចូលចិត្ដធ្វើល្អនឹង អ្នកដទៃតែចំពោះគ្រួសាររបស់គេវិញ គេហ៊ានលះបង់គ្រប់យ៉ាងដើម្បីផ្គត់ផ្គង់ ។ គេជាអ្នកមានមនៈសិការហើយគត់មត់ពិសេសចំពោះការណាដែលទាក់ទ")
# pd.insert(27, 6, 2, "គេមាននិស្ស័យជាអ្នកស្ងប់ស្ងៀមហើយនឹងធឹងព្រមទាំងស្លូតបូតនិងសោះ អង្គើយជាមួយនឹងអាការៈស្ងប់ស្ងៀមនិងអត់ធ្មត់ ។ មនុស្សជំពូកលេខ៦ច្រើនតែធ្វើឱ្យអ្នកផងរាប់អានណាស់តែក្នុងចំណោមជនខាងក្រោយនេះគ្មានជនណាម្នាក់ហ៊ានអះអាងថាបានស្គាល់គំនិតរបស់មនុស្សឱ្យបាន ច្បាស់លាស់ទេ ។ ការពិតបើ")
# pd.insert(28, 6, 3, "មនុស្សជំពូកលេខ៦មិនងាយដាក់ចិត្ដស្រឡាញ់គេផ្ដេសផ្ដាសទេតែបើបានជាចាប់ចិត្ដស្រឡាញ់ហើយគឺស្លាប់ទៅយកទៅផង ។ បើបានជារៀបការនឹងអ្នកណាមួយហើយមនុស្សនេះថ្នាក់ថ្នមគេគ្រប់បែបយ៉ាង ហើយមិនព្រមឱ្យគូស្រកររវើរវាយក្រៅពីខ្លួនទេ ។ គំនិតចង់បានតែម្នាក់ឯងនេះជាការមួយមិនគួរគាប់ទេប៉ុន្ដែគ")
# pd.insert(29, 6, 4, "មនុស្សជំពូកលេខ៦មិនសូវជាអ្នកមានចិត្ដលោភទេអ៊ីចឹងហើយបានគេកើតមកមិនពូកែខាងការជជែកវែកញែកដែលត្រូវការឱ្យមានគំនិតផ្ដួចផ្ដើមនិងបញ្ចេញបញ្ចូល ។ បំណងខាងបញ្ហាមនុស្សតែងជំរុញមនុស្សនេះឱ្យចូលចិត្ដធ្វើការណា ដែលទាក់ទង នឹងសង្គមដូចជាគ្រូពេទ្យឧបការីសង្គមនិងសាស្ដ្រាចារ្យជាដើម ។ ")
# pd.insert(30, 6, 5, "គេមិនសូវឃើញមនុស្សជំពូកលេខ៦នេះមានទ្រព្យជាដុំកំភួនទេព្រោះមនុស្ស នេះគ្មានចិត្ដស្រេកឃ្លានចង់មានចង់បានឡើយមានប៉ុន្មានស៊ីប៉ុណ្ណឹង ។ គេមិនមែនជាអ្នកចាយវាយធំទេប៉ុន្ដែគេក៏មិនឱ្យតម្លៃធំទៅលើរឿងលុយកាក់ដែរ ។")
# pd.insert(31, 7, 1, "មានប្រាជ្ញាឆ្លាតឆ្លុំឆាប់យល់មិនងាយជឿរឿងអ្វីមួយៗ ដោយងាយទេ ។ បើនឹងជឿលុះណាតែបានពិចារណាបានដិតដល់ណាស់ ។ គេមិនចូលចិត្ដការងារណាដែលមិនស្របនឹងគំនិតប្រាជ្ញារបស់គេទេ ។")
# pd.insert(32, 7, 2, "ជាអ្នកម៉ឺងម៉ាត់ បើនឹងអារកាត់រឿងអ្វីមួយគេច្រើនតែធ្វើឡើងដោយ វិចារណញ្ញាណគឺមិនមែនដោយផ្លូវចិត្ដទេ ។ គេជាមិត្ដភក្ដិម្នាក់ចេះស្គាល់ទុក្ខធុរៈចេះយោគយល់គ្នាទៅវិញទៅមកមិនងាយប្រកាន់ខឹងតែបើបានជាប្រកាន់ ខឹងហើយក៏មិនងាយជានាវិញដែរ ។ គេជាមនុស្សគួរឱ្យទុកចិត្ដរាប់អានបានព្រោះម")
# pd.insert(33, 7, 3, "ដោយគេជាមនុស្សមានប្រាជ្ញាគេមិនសូវខកចិត្ដក្នុងរឿងគូស្រករទេគេច្រើន រើសបានគូគាប់ស្របតាមសេចក្ដីប្រាថ្នារបស់គេ ។ គេមិនចូលចិត្ដរើសគូស្រករណាដែលមិនឆ្លាតឆ្លុំឡើយ ។ យកល្អត្រូវរៀបការជាមួយនឹងមនុស្សជំពូកលេខ៩ និងលេខ៤ព្រោះប្រាជ្ញា និងចិត្ដជាអ្នកមនុស្សនិយមមានស្របគ្នា ។ មិ")
# pd.insert(34, 7, 4, "មនុស្សនេះចូលចិត្ដស្រឡាញ់ការងារណា ដែលប្រើប្រាជ្ញា ។ គេច្រើនជាសង្គមវិទូ សិល្បករ មេធាវី រដ្ឋបាល ឬពាណិជ្ជករ ។ ជាទូទៅ ក្នុងមុខរបរគេច្រើនបានទទួលជោគជ័យរហ័សណាស់ ។")
# pd.insert(35, 7, 5, "គេមិនជាអ្នកចាយធូរ តែក៏មិនជាអ្នកកំណាញ់ដែរ ។ កិច្ចការណាត្រូវចាយទើប គេចាយ ។ និយាយឱ្យខ្លីទៅ គឺគេចេះចាយមានមុខមានបែប ។ គេមិនសូវជួបប្រទះនឹងរឿងទាល់លុយកាក់ទេហើយក៏ច្រើនហ៊ានចាយវាយជួយមិត្ដភក្ដិដែលជួបប្រទះនឹងការលំបាកផ្នែកហិរញ្ញវត្ថុទៀតផង ។")
# pd.insert(36, 8, 1, "ជាមនុស្សប្រកបដោយកំលាំងខាងឆន្ទៈរកមិនបាន ហើយមានចរិតរឹងដូចដែក ។ ទុកចិត្ដខ្លួនឯងណាស់ហើយបើនឹងកាន់ការអ្វីមួយហើយគឺធ្វើឱ្យទាល់តែបាន សំរេចទើបសុខចិត្ដ ។ មិនចេះសំលុតគេហើយបើជួបប្រទះនឹងការពិបាកអ្វីមួយនៅពេលកំពុងចង់ សំរេចបំណងអ្វីមួយហើយមនុស្សនេះឥតចេះរាថយឬក៏ខកចិត្ដទេគឺពុះ")
# pd.insert(37, 8, 2, "គេជាមនុស្សមានគំនិតប្រយុទ្ធហើយស្វាហាប់ហ៊ានតស៊ូយ៉ាងពេញទំហឹងដើម្បី ការពារឧត្ដមគតិដែលខ្លួនជឿថាល្អ ។ មានចិត្ដលោភលន់ហើយស្វិតស្វាញ ។ បើចង់សំរេចគោលបំណងអ្វីមួយហើយមនុស្សលេខ៨សុខចិត្ដលះបង់គោល បំណងដទៃទៀតចោលសិន ដើម្បីធ្វើគោលបំណងនេះឱ្យទាល់តែបានសំរេច ។ អ៊ីចឹងហើយ បានជាមាន")
# pd.insert(38, 8, 3, "ក្នុងរឿងស្នេហាមនុស្សជំពូកលេខ៨ ច្រើនប្រែប្រួលមិននឹងហ្នទេ ។ មានម្ង៉ៃថ្នាក់ថ្នមគូគាប់មានម្ង៉ៃទៀតបែបរៀងគេចៗហើយបែបវាហី ។ ដោយហេតុមនុស្សនេះមានចរិតពិបាកបែបនេះមនុស្សជំពូកលេខ៨ ត្រូវរក គូស្រករណាដែលចេះយល់ខ្លួនចេះអត់ឱនចំពោះទឹកមុខប្រែប្រួលគ្មានឈប់ឈរ របស់ខ្លួន ។ ជាទូទៅគ")
# pd.insert(39, 8, 4, "ដោយហេតុមាននិស្ស័យខាងគំនិតបង្កើតច្រើន និងប្រកបដោយថាមពល អស្ចារ្យទៀតនោះមនុស្សជំពូកលេខ៨ត្រូវវាសនាចារមកឱ្យបានទទួលជោគជ័យក្នុងកិច្ចការសព្វសារពើ ។ តែធ្វើអ្វីហើយគឺធ្វើដោយមធ្យ័តបំផុត ។")
# pd.insert(40, 8, 5, "គេជាមនុស្សពូកែខាងយកលុយទៅរកស៊ីណាស់ ។ ទោះជាសម្បត្ដិទ្រព្យរបស់ មានធំឬតូចក៏ដោយឱ្យតែគេប្រកបរបរគេមិនងាយខូចខាតលុយកាក់ទេ ។ មនុស្សធំៗ ជាច្រើនដែលស្ថិតនៅក្នុងជំពូកមនុស្សលេខ៨នេះ ច្រើនរក ទ្រព្យសម្បត្ដិបានស្ដុកស្ដមណាស់ ដោយចាប់រកស៊ីពីគ្មានមួយសេនទៅ ។")
# pd.insert(41, 9, 1, "គឺជាមនុស្សប្រកបដោយភាពរំភើបដ៏ជ្រាលជ្រៅនិងមនុស្សធម៌ដ៏អស្ចារ្យ ។ ជាមនុស្សចិត្ដល្អណាស់ឱ្យតែមានគេមកសុំជំនួយភ្លាមគឺជួយគេដោយឥឥតគិត ផលប្រយោជន៍ទេ ។ គេជាអ្នកឧត្ដមគតិនិយមផងប្រលោមនិយមផងអញ្ចឹងហើយបានជាគេជា មនុស្សចូលចិត្ដមើលឃើញអ្នកដទៃល្អហើយស្មោះត្រង់ ។ គឺគេទុកចិត្ដលើ មន")
# pd.insert(42, 9, 2, "ដោយហេតុគេមាននិស្ស័យស្រស់ស្រាយហើយចូលចំណោមចុះនោះមនុស្សជំពូកលេខ៩តែងមានមិត្ដភក្ដិច្រើនក៏ប៉ុន្ដែគេក៏តែងឃើញមនុស្សនេះមានសត្រូវខ្លះ ដែរ ។ ជាការផ្ទុយដែលជួនកាលមនុស្សនេះមានប្រតិកម្មបែបជាអ្នកការទូតឬក៏ មិននិយាយការពិតប្រាប់គេឯង ។ មិនជាអ្នកម៉ត់ចត់ទេតែទោះជាយ៉ាងណាក៏មនុស្ស")
# pd.insert(43, 9, 3, "ជាអ្នកមានចិត្ដស្មោះត្រង់ក្នុងស្នេហាគឺជាគូស្រករដ៏ឧត្ដមថ្វីបើពេលខ្លះមនុស្ស ជំពូកនេះមិនរវីរវល់នឹងការថ្នាក់ថ្នមគ្រួសារព្រោះតែខ្លួនជាប់រវល់ នឹង ប្រយោជន៍ដ៏ច្រើនហើយប្លែកក្ដី ។ យកល្អមនុស្សជំពូកលេខ៩ត្រូវរៀបការជាមួយមនុស្សជំពូកលេខ៩ ដូចគ្នា លេខ៧ ឬលេខ៤ ។ គូស្រករបែបនេះ")
# pd.insert(44, 9, 4, "មនុស្សជំពូកលេខ៩ ចូលចិត្ដតែការងារណាដែលនាំឱ្យអាចរស់នៅជាមួយអ្នក ផងបានរហូតព្រោះមនុស្សជំពូកនេះ ចូលចិត្ដទាក់ទងនឹងធ្វើសហការជាមួយ អ្នកដទៃណាស់ ។ គេច្រើនតែធ្វើជាចៅក្រម មេធាវី គ្រូពេទ្យ ឬសាស្ដ្រាចារ្យ ។ យកល្អមនុស្សជំពូកលេខ៩ គួរកាន់កាប់មុខរបរទាំងនេះ ។")
# pd.insert(45, 9, 4, "ក្នុងរឿងរកលុយកាក់មនុស្សជំពូកលេខ៩មិនពូកែទាល់តែសោះ ។ តែគេច្រើនជាមនុស្សមានសំណាងក្នុងរឿងរកលុយកាក់ទៅវិញ ហើយជាមនុស្សចិត្ដល្អ ចំពោះអ្នកខ្វះខាត ។")
