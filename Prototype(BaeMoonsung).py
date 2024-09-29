class User:
    def __init__(self, name, username, password, role):
        self.name = name
        self.username = username
        self.password = password
        self.role = role

    def intro(self):
        print("Are you an Applicant or HQ Officer? (App or HQ) :", end=" ")
        flog = input("")
        if flog == "App":
            a1.login()
        elif flog == "HQ":
            h1.login()
        else:
            print("Enter Courrectly Please", "Try again")
            s1.intro()

    def login(self):
        print("[[Login]]")
        u = input("Username : ")
        p = input("Password : ")
        if u == self.username and p == self.password and self.role == "APPLICANT":
            print('\n'
                  "Hello", self.name, "!!",
                  "Welcome to Job Application System")
            a1.applogin()

        elif u == self.username and p == self.password and self.role == "HQ":
            print('\n'
                  "Hello", self.name, "HQ_Officer !!",
                  "Welcome to Job Application System")
            h1.hq_main()

        else:
            print("Incorrect Username or Password")
            s1.intro()


#노쓸모 클래스
class Application:
    dateApplied = str()
    positionApplied = str()
    expectedSalary = str()
    availability = str()

    def add_app(self):
        print("Please fill out the below fields.")

        Application.dateApplied = input("Date Applied : ")
        Application.positionApplied = input("Position Applied : ")
        Application.expectedSalary = input("Expected Salary(SGD) : ")
        Application.availability = input("Availiability[Month(s)] : ")

        if len(Application.dateApplied) and len(
                Application.positionApplied) and len(
                    Application.expectedSalary) and len(
                        Application.availability) > 0:
            print('\n'
                  "Please Confirm  ", '\n', "Date Applied    : ",
                  Application.dateApplied, '\n', "PositionApplied : ",
                  Application.positionApplied, '\n', "Expected Salary : ",
                  Application.expectedSalary, '\n', "Availiability   : ",
                  Application.availability)

            a1.add_Per()
        else:
            print('\n' "All fields must be filled.", '\n' "Please try again")
            a1.add_app()


#노쓸모 클래스
class Personal_Details:
    name = str()
    NIRC_passport = str()
    address = str()
    postcode = str()
    email = str()
    phoneNo = str()
    dateofBirty = str()
    mobileNo = str()
    gender = str()

    def add_Per(self):
        print('\n' "Please fill out the Personal Details")

        Personal_Details.name = input("Name : ")
        Personal_Details.NIRC_passport = input("NIRC_passport : ")
        Personal_Details.address = input("Address : ")
        Personal_Details.postcode = input("Postcode : ")
        Personal_Details.email = input("Email : ")
        Personal_Details.phoneNo = input("PhoneNo : ")
        Personal_Details.dateofBirty = input("Date of Birth : ")
        Personal_Details.mobileNo = input("MobileNo : ")
        Personal_Details.gender = input("Gender(Male or Female) : ")

        if len(Personal_Details.name) and len(
                Personal_Details.NIRC_passport) and len(
                    Personal_Details.address) and len(
                        Personal_Details.postcode) and len(
                            Personal_Details.email) and len(
                                Personal_Details.phoneNo) and len(
                                    Personal_Details.dateofBirty) and len(
                                        Personal_Details.mobileNo) and len(
                                            Personal_Details.gender) > 0:
            print('\n'
                  "Please Confirm  ", '\n', "Name          : ",
                  Personal_Details.name, '\n', "NIRC_passport : ",
                  Personal_Details.NIRC_passport, '\n', "Address       : ",
                  Personal_Details.address, '\n', "Postcode      : ",
                  Personal_Details.postcode, '\n', "Email         : ",
                  Personal_Details.email, '\n', "PhoneNo       : ",
                  Personal_Details.phoneNo, '\n', "Date of Birty : ",
                  Personal_Details.dateofBirty, '\n', "MobileNo      : ",
                  Personal_Details.mobileNo, '\n', "Gender        : ",
                  Personal_Details.gender)
            a1.add_Qual()
        else:
            print('\n' "All fields must be filled.", '\n' "Please try again")
            a1.add_Per()


#노쓸모 클래스
#At least one Qualification
class Qualifications:
    qualification = []
    institution_Uni = []
    major = []
    grade = []
    yearGraduated = []

    def add_Qual(self):

        while True:
            print('\n' "Please fill out al least one Qualifications")

            Qualifications.qualification.append(input("Qualification : "))
            Qualifications.institution_Uni.append(
                input("Institution/University : "))
            Qualifications.major.append(input("Mojor : "))
            Qualifications.grade.append(input("Grade : "))
            Qualifications.yearGraduated.append(input("Year Graduated : "))

            e = input("Do you want to fill out more Qualifications?(Y/N) : ")
            if e == "Y":
                continue
            elif e == "N" and len(Qualifications.qualification) and len(
                    Qualifications.institution_Uni) and len(
                        Qualifications.major) and len(
                            Qualifications.grade) and len(
                                Qualifications.yearGraduated) > 0:
                #break
                a1.confirm()

                a1.add_Work()
                break
            else:
                print("Please enter correctly")
                continue

    def confirm(self):
        if len(Qualifications.qualification) and len(
                Qualifications.institution_Uni) and len(
                    Qualifications.major) and len(
                        Qualifications.grade) and len(
                            Qualifications.yearGraduated) > 0:
            print('\n'
                  "Please Confirm  ", '\n', "Qualification            : ",
                  Qualifications.qualification, '\n',
                  "Institution / University : ",
                  Qualifications.institution_Uni, '\n',
                  "Mojor                    : ", Qualifications.major, '\n',
                  "Grade                    : ", Qualifications.grade, '\n',
                  "Year Graduated           : ", Qualifications.yearGraduated)
        # a1.add_work()

        else:
            print("All fields must be filled.", '\n' "Please try again")
            a1.add_Per()


#노쓸모 클래스
#선택사항
class WorkingEx:
    company = []
    industry = []
    position = []
    _from = []
    _to = []
    level = []
    monthlySalary = []

    def add_Work(self):

        print('\n' "Please fill out the Work Experiences")

        while True:
            WorkingEx.company.append(input("Company : "))
            WorkingEx.industry.append(input("Industry : "))
            WorkingEx.position.append(input("Position : "))
            WorkingEx._from.append(input("From : "))
            WorkingEx._to.append(input("To : "))
            WorkingEx.level.append(
                input(
                    "Level\n(Non_Executive, Fresh/Entry Level, Junior Excutive, Senior Executive, Manager, Senior Manager)\n : "
                ))
            WorkingEx.monthlySalary.append(input("Monthly Salary : "))

            e = input("Do you want to fill out more Work Experiences?(Y/N) : ")
            if e == "Y":
                continue
            elif e == "N":
                print('\n'
                      "Please Confirm  ", '\n', "Company      : ",
                      WorkingEx.company, '\n', "Industry     : ",
                      WorkingEx.industry, '\n', "Position     : ",
                      WorkingEx.position, '\n', "From         : ",
                      WorkingEx._from, '\n', "To           : ", WorkingEx._to,
                      '\n', "Level        : ", WorkingEx.level)

                a1.add_Refer()
                break

            else:
                print("Please enter correctly")


# 2개#노쓸모 클래스
class References:
    name = []
    occupation = []
    company_organ = []
    contactNo = []
    email = []
    relationship = []

    def add_Refer(self):

        while True:
            print('\n' "Please fill out 2 of References")
            References.name.append(input("Name : "))
            References.occupation.append(input("Institution/University : "))
            References.company_organ.append(input("Mojor : "))
            References.contactNo.append(input("Contact Number : "))
            References.email.append(input("Email : "))
            References.relationship.append(input("Relationship : "))

            if len(References.name) and len(References.occupation) and len(
                    References.company_organ) and len(
                        References.contactNo) and len(
                            References.email) and len(
                                References.relationship) == 2:
                print('\n'
                      "Please Confirm  ", '\n', "Name                   : ",
                      References.name, '\n', "Occupation             : ",
                      References.occupation, '\n', "Company / Organization : ",
                      References.company_organ, '\n',
                      "Contact Number         : ", References.contactNo, '\n',
                      "Email                  : ", References.email, '\n',
                      "Relationship           : ", References.relationship,
                      '\n',
                      "Your Application Form has been created successfully.")
                a1.submit()

                break
            elif len(References.name) and len(References.occupation) and len(
                    References.company_organ) and len(
                        References.contactNo) and len(
                            References.email) and len(
                                References.relationship) < 2:
                print("You need to fill out 2 of References")
                continue

        else:
            print("All fields must be filled.", '\n' "Please try again")
            a1.add_Per()


class Infosys:

    vacancy = int()
    submittedNo = int()
    result = int()

    #  self.isthere = isthere
    #  self.submitted = submitted

    def add_vacancy(self):

        Infosys.vacancy = Infosys.vacancy + int(
            input("\nHow many Vacancy you want to add? : "))

        print('\n' "The number of Current Vacancies is", Infosys.vacancy)
        h1.hq_login2()
        return Infosys.vacancy

    def hq_login2(self):
        print('\n' "Applied successfully" '\n')
        z = input(
            "Do you want to Confirm the current vacancy you added or Add more vacancy or Go back to Mainpage(Confirm or Add or Go) \n: "
        )
        if z == "Confirm":
            print("The number of Current Vacancies is", Infosys.vacancy)

            print("Enter to go Mainpage")
            h1.hq_main()

        elif z == "Add":
            h1.add_vacancy()

        elif z == "Go":
            h1.hq_main()


class HQ_Officer(User, Infosys, Application, Personal_Details, Qualifications,
                 WorkingEx, References):
    def review(self):

        if Infosys.submittedNo > 0:

            print(" Date Applied    : ", Application.dateApplied, '\n',
                  "PositionApplied : ", Application.positionApplied, '\n',
                  "Expected Salary : ", Application.expectedSalary, '\n',
                  "Availiability   : ", Application.availability)

            print('\n' "[Personal Details]")
            print(" Name          : ", Personal_Details.name, '\n',
                  "NIRC_passport : ", Personal_Details.NIRC_passport, '\n',
                  "Address       : ", Personal_Details.address, '\n',
                  "Postcode      : ", Personal_Details.postcode, '\n',
                  "Email         : ", Personal_Details.email, '\n',
                  "PhoneNo       : ", Personal_Details.phoneNo, '\n',
                  "Date of Birty : ", Personal_Details.dateofBirty, '\n',
                  "MobileNo      : ", Personal_Details.mobileNo, '\n',
                  "Gender        : ", Personal_Details.gender)

            print('\n' "[Qualifications]")
            print(" Qualification            : ", Qualifications.qualification,
                  '\n', "Institution / University : ",
                  Qualifications.institution_Uni, '\n',
                  "Mojor                    : ", Qualifications.major, '\n',
                  "Grade                    : ", Qualifications.grade, '\n',
                  "Year Graduated           : ", Qualifications.yearGraduated)

            print('\n' "[Work Experiences]")
            print(" Company      : ", WorkingEx.company, '\n',
                  "Industry     : ", WorkingEx.industry, '\n',
                  "Position     : ", WorkingEx.position, '\n',
                  "From         : ", WorkingEx._from, '\n', "To           : ",
                  WorkingEx._to, '\n', "Level        : ", WorkingEx.level)

            print('\n' "[References]")
            print("Name                   : ", References.name, '\n',
                  "Occupation             : ", References.occupation, '\n',
                  "Company / Organization : ", References.company_organ, '\n',
                  "Contact Number         : ", References.contactNo, '\n',
                  "Email                  : ", References.email, '\n',
                  "Relationship           : ", References.relationship)

            a = input("Press enter to produce the review results.")
            if a == '':
                h1.make_result()

        else:
            print("There is no Submitted Application Form")
            h1.hq_main()

    dateReceived = str()
    nameofHROfficer = str()
    outcome = str()
    reason = str()
    resultdate = str()

    def make_result(self):

        while True:
            print('\n' "Please fill out the fields below.")
            HQ_Officer.dateReceived = input("Date Received : ")
            HQ_Officer.nameofHROfficer = input("HR Officer : ")
            HQ_Officer.outcome = input(
                "Outcome\n(Discard / Keep for Future / Insufficient Documents / Call for Interview / Offer without Interview)\n: "
            )
            HQ_Officer.reason = input("Reason(optional) : ")
            HQ_Officer.resultdate = input("Date : ")

            if len(HQ_Officer.dateReceived) and len(
                    HQ_Officer.nameofHROfficer) and len(
                        HQ_Officer.outcome) and len(self.resultdate) > 0:

                print('\n'
                      "Please Confirm  ", '\n', "Date Received : ",
                      HQ_Officer.dateReceived, '\n', "HR Officer    : ",
                      HQ_Officer.nameofHROfficer, '\n', "Outcome       : ",
                      HQ_Officer.outcome, '\n', "Reason        : ",
                      HQ_Officer.reason, '\n', "Date           : ",
                      HQ_Officer.resultdate)
                print(
                    "Your Review of the Application Form has been created successfully."
                    '\n')
                Infosys.result = Infosys.result + 1
                h1.hq_main()

                break
            else:
                print("Please fill out properly the mandatory fields")
                continue

    def hq_main(self):
        print("The number of Current Vacancies is", Infosys.vacancy)
        print("The number of submitted Application form by Applicants : ",
              Infosys.submittedNo)
        z = input(
            '\n'
            "Do you want to add new job vacancy or review or login again?\n(Add / Review / Login) : "
        )
        if z == "Add":
            h1.add_vacancy()
        elif z == "Login":
            s1.intro()
        elif z == "Review":
            h1.review()


h1 = HQ_Officer("Yenie", "HQ_Officer1", "1205", "HQ")

#그냥 음 .. 사랑해 ♥


class Staff(User):
    def start_sys(self):
        print("Welcome!!!")
        print("----loading-----")


s1 = Staff("Bae", "staff22", "0628", "STAFF")


class Applicant(User, Infosys, Application, Personal_Details, Qualifications,
                WorkingEx, References):
    def applogin(self):
        print("The Number of current Vacancy: ", Infosys.vacancy)
        print("The Number of Application form you submitted : ",
              Infosys.submittedNo)
        print("The Number of Result of review : ", Infosys.result)
        ans = input(
            "Do you want to Re-Login or Apply or Check the result of review?\n(Login / Apply / Check) :"
        )

        if ans == "Apply" and Infosys.vacancy > 0:
            a1.add_app()

        elif ans == "Apply" and Infosys.vacancy == 0:
            print("Sorry, There is no Vacancy yet.")
            a1.applogin()

        elif ans == "Check" and Infosys.result > 0:
            print('\n'
                  "Please Confirm  ", '\n', "Date Received : ",
                  HQ_Officer.dateReceived, '\n', "HR Officer    : ",
                  HQ_Officer.nameofHROfficer, '\n', "Outcome       : ",
                  HQ_Officer.outcome, '\n', "Reason        : ",
                  HQ_Officer.reason, '\n', "Date           : ",
                  HQ_Officer.resultdate)
            a1.applogin()

        elif ans == "Check" and Infosys.result == 0:
            print("Sorry, There is Result of Review yet.")
            a1.applogin()

        elif ans == "Login":
            s1.intro()

        else:
            print("Please Answer Courrectly")
            a1.applogin()

    def submit(self):
        a = input('\n' "Do you want to submit the application form? (Y/N) : ")
        if a == "Y":
            Infosys.submittedNo = Infosys.submittedNo + 1
            print("Submitted successfully")
            a1.applogin()
        elif a == "N":
            s1.intro()


a1 = Applicant("July", "086la980", "0486", "APPLICANT")

s1.start_sys()

s1.intro()
