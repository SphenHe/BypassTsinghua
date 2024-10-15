//不要仇恨抽象的人，要去感受具体的爱

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

#ifdef _WIN32
#define CLEAR "cls"
#else
#define CLEAR "clear"
#endif

// Constants
const int ALL_USERS=1000;                               // The max number of the users
const int ALL_LOG=1000;                                 // The max record of the log

const int NAME_LENGTH=20;                               // The max length of the name
const int PASSWORD_LENGTH=20;                           // The max length of the password
const int PHONE_LENGTH=20;                              // The max length of the phone number
const int DONATION_LENGTH=100;                          // The max length of the objects of the donation
const int PURPOSE_LENGTH=100;                           // The max length of the purpose of the donation
const int REASON_LENGTH=100;                            // The max length of the reason of the request
const int SOURCE_LENGTH=100;                            // The max length of the source of the supply

// Structures
struct time
{
    int year;
    int month;
    int day;
    int hour;
    int start_day;
    int start_hour;
    int end_day;
    int end_hour;
};

struct id                                                                       // Used to store the id
{
    int status;                                                                 // -1: deleted 0: none 1: admin 2: manager 3: alumni 4: teacher 5: student 6: workers 7: guest
    char name[NAME_LENGTH];
    char password[PASSWORD_LENGTH];
};
struct id Users[ALL_USERS];                                                     // Used to store all the users

struct visitor
{
    int user;                                                                   // The user id
    int is_approved;                                                            // 0: not approved 1: approved
    char name[NAME_LENGTH];                                                     // The name of the visitor
    char phone[PHONE_LENGTH];                                                   // The phone number of the visitor
    char purpose[PURPOSE_LENGTH];                                               // The purpose of the donation
    struct time time;                                                           // The department of the donation
};
struct visitor Visitors[ALL_USERS];                                             // Used to store all the visitors

struct donation
{
    char name[NAME_LENGTH];                                                     // The name of the donor
    char phone[PHONE_LENGTH];                                                   // The phone number of the donor
    char donation[DONATION_LENGTH];                                             // The objects of the donation
    char purpose[PURPOSE_LENGTH];                                               // The purpose of the donation
    int department;                                                             // The department of the donation
    int money;                                                                  // The money of the donation
};
struct donation Donations[ALL_USERS];                                           // Used to store all the donations

struct activities
{
    // People
    int all_people;
    int id[10];
    char group[NAME_LENGTH];
    // Activity
    char name[NAME_LENGTH];                                                     // The name of the activity
    char place[NAME_LENGTH];                                                    // The place of the activity
    char content[NAME_LENGTH];                                                  // The content of the activity
    struct time activitytime;                                                           // The time of the activity
    // Approval
    int is_approvaed;                                                               // 0: not approved 1: approved
    struct time approvaltime;                                                           // The time of the approval
    int approver;                                                         // The approver
    // Grants
    int is_grant;                                                               // 0: not grant 1: grant
    int grant;                                                                  // The grant of the activity
};
struct activities Activities[ALL_USERS];                                        // Used to store all the activities

struct gala
{
    int user;
    int status;                                                                 // 0: not approved 1: approved
    int ranum;
};
struct gala GalacticTickets[ALL_USERS];                                         // Used to store all the galatickets

struct supply
{
    int action;// 1:add 2:request
    int supply;// 1:Mask 2:Bag 3:Tag 4:Notebook
    int number;//
    int user;// The user id
    int approver;// The approver id
    struct time time;
    char source[NAME_LENGTH];
};
struct supply Supplies[ALL_LOG];                                              // Used to store all the supplies

// Configurations
int CurrentUser=0;                                                              // Used to know who is using the program

int AllUsers=0;                                                                 // Used to know how many users are there

int AllDonations=0;                                                             // Used to know how many donations are there
int AllGalaTickets=1000;                                                           // Used to know how many galatickets are there
int AllGalacticTicketsRequests=0;                                               // Used to know how many galatickets requests are there
int AllVisitingRequests=0;                                                              // Used to know how many visitors are there
int AllVisitors=1000;                                                            // Used to know how many visitors are there
int Alnumivisitors=0;                                                            // Used to know how many visitors are there
int Guestvisitors=0;                                                            // Used to know how many visitors are there
int ALLalnumivisitors=0;                                                            // Used to know how many visitors are there
int ALLguestvisitors=0;                                                            // Used to know how many visitors are there
int AllActivityRequests=0;                                                      // Used to know how many activity requests are there
int AllSupplyLogs=0;                                                            // Used to know how many supply logs are there

int sup[5]={0,0,0,0,0};

// Usefull functions
void InputControl(const int INPUT_LENGTH,char* p,const char* q);                //Input control
void PrintFile(const char* filename,const char* notice);                        // Print the file
void PressEnterToContinue();

// Other functions
void Init();
void LoginPage();                                                               // Initialize all the things
void Save();                                                                    // Save all the things

// Different menus
void AdminMenu();
    void AddUser();
    void DeleteUser();
        void IDFileWrite();
    void SetConfig();

void ManagerMenu();
    void AddVisitor();
    void ApproveActivity();
    void ApproveActivityGrant();
    void ApproveVisitor();
    void DonationSort();
    void DonationList();
    void GalaTicketLottery();
    void SupplyControl(int option);
    void ShowLog();

void AlumniMenu();
    void AddDonation();
        void DonationFileWrite();
    void CheakGalaTicket();
    void RequestGalaTicket();
        void GalaTicketFileWrite();
    void RequestVisiting();
    void SupplyControl(int option);

void TeacherMenu();
    void ApproveActivityGrant();
    void CheakGalaTicket();
    void RequestGalaTicket();

void StudentMenu();
    void CheakActivity();
    void CheakGalaTicket();
    void RequestActivity();
    void RequestGalaTicket();

void WorkersMenu();
    void ApproveVisitorCheak();
    void CheakGalaTicket();
    void SupplyControl(int option);
    void RequestGalaTicket();

void GuestMenu();
    void CheakGalaTicket();
    void CheakVisiting();
    void RequestGalaTicket();
    void RequestVisiting();

void Register();

int main()//Main function
{
    system(CLEAR);
    Init();
    system(CLEAR);
    PrintFile("welcome.txt","");
    PressEnterToContinue();
    while(1)
    {
        LoginPage();
        switch (Users[CurrentUser].status)
        {
            case 8:system(CLEAR);PrintFile("exitpage.txt","");PressEnterToContinue();return 0;
            case 0:break;
            case 1:AdminMenu();break;
            case 2:ManagerMenu();break;
            case 3:AlumniMenu();break;
            case 4:TeacherMenu();break;
            case 5:StudentMenu();break;
            case 6:WorkersMenu();break;
            case 7:GuestMenu();break;
            default:break;
        }
        CurrentUser=0;
    }
    return 0;
}

void Init()//Initialize all the things
{
    //id.txt
    system(CLEAR);
    FILE* id=fopen("id.txt","r");
    if(id==NULL)
    {
        printf("Can't open the file!\n");
        exit(1);
    }
    fscanf(id,"CurrentUser=%d\n",&AllUsers);
    for(int i=0;i<AllUsers+1;i++)
    {
        fscanf(id,"{%d,\"%[^\"]\",\"%[^\"]\"};\n",&Users[i].status,Users[i].name,Users[i].password);
    }
    fclose(id);
    //donation.txt
    FILE* donation=fopen("donation.txt","r");
    if(donation==NULL)
    {
        printf("Can't open the file!\n");
        exit(1);
    }
    fscanf(donation,"CurrentDonation=%d\n",&AllDonations);
    for(int i=1;i<AllDonations+1;i++)
    {
        fscanf(donation,"{\"%[^\"]\",\"%[^\"]\",\"%[^\"]\",\"%[^\"]\",%d};\n",Donations[i].name,Donations[i].phone,Donations[i].donation,Donations[i].purpose,&Donations[i].department);
    }
    fclose(donation);
    //gala.txt
    FILE* galactic_tickets=fopen("gala.txt","r");
    if(galactic_tickets==NULL)
    {
        printf("Can't open the file!\n");
        exit(1);
    }
    fscanf(galactic_tickets,"AllGalacticTicketsRequests=%d\n",&AllGalacticTicketsRequests);
    for(int i=1;i<AllGalacticTicketsRequests+1;i++)
    {
        fscanf(galactic_tickets,"{%d,%d,%d};\n",&GalacticTickets[i].user,&GalacticTickets[i].status,&GalacticTickets[i].ranum);
    }
    fclose(galactic_tickets);
    //visitior.txt
    FILE* visitor=fopen("visiting.txt","r");
    if(visitor==NULL)
    {
        printf("Can't open the file!\n");
        exit(1);
    }
    fscanf(visitor,"AllVisitingRequests=%d\n",&AllVisitingRequests);
    for(int i=1;i<AllVisitingRequests+1;i++)
    {
        fscanf(visitor,"{%d,%d,\"%[^\"]\",\"%[^\"]\",\"%[^\"]\",{%d,%d,%d}};\n",&Visitors[i].user,&Visitors[i].is_approved,Visitors[i].name,Visitors[i].phone,Visitors[i].purpose,&Visitors[i].time.year,&Visitors[i].time.month,&Visitors[i].time.day);
    }
    fclose(visitor);
    //activities.txt
    FILE* activity=fopen("activities.txt","r");
    if(activity==NULL)
    {
        printf("Can't open the file!\n");
        exit(1);
    }
    fscanf(activity,"AllActivityRequests=%d\n",&AllActivityRequests);
    for(int i=1;i<AllActivityRequests+1;i++)
    {
        fscanf(activity,"{%d,{%d",&Activities[i].all_people,&Activities[i].id[0]);
        for(int j=1;j<10;j++)
        {
            fscanf(activity,",%d",&Activities[i].id[j]);
        }
        fscanf(activity,"},\"%[^\"]\",",Activities[i].group);
        //fscanf(activity,"{\"%[^\"]\",\"%[^\"]\",\"%[^\"]\",{%d,%d,%d,%d,%d,%d,%d},%d,{%d,%d,%d,%d,%d,%d,%d},%d,%d,%d};\n",Activities[i].name,Activities[i].place,Activities[i].content,&Activities[i].activitytime.year,&Activities[i].activitytime.month,&Activities[i].activitytime.day,&Activities[i].activitytime.start_day,&Activities[i].activitytime.start_hour,&Activities[i].activitytime.end_day,&Activities[i].activitytime.end_hour,&Activities[i].is_approvaed,&Activities[i].approvaltime.year,&Activities[i].approvaltime.month,&Activities[i].approvaltime.day,&Activities[i].approvaltime.start_day,&Activities[i].approvaltime.start_hour,&Activities[i].approvaltime.end_day,&Activities[i].approvaltime.end_hour,&Activities[i].approver,&Activities[i].is_grant,&Activities[i].grant);
        fscanf(activity,"\"%[^\"]\",\"%[^\"]\",\"%[^\"]\",{%d,%d,%d,%d,%d,%d,%d},%d,{%d,%d,%d,%d,%d,%d,%d},%d,%d,%d};\n",Activities[i].name,Activities[i].place,Activities[i].content,&Activities[i].activitytime.year,&Activities[i].activitytime.month,&Activities[i].activitytime.day,&Activities[i].activitytime.start_day,&Activities[i].activitytime.start_hour,&Activities[i].activitytime.end_day,&Activities[i].activitytime.end_hour,&Activities[i].is_approvaed,&Activities[i].approvaltime.year,&Activities[i].approvaltime.month,&Activities[i].approvaltime.day,&Activities[i].approvaltime.start_day,&Activities[i].approvaltime.start_hour,&Activities[i].approvaltime.end_day,&Activities[i].approvaltime.end_hour,&Activities[i].approver,&Activities[i].is_grant,&Activities[i].grant);
    }
    fclose(activity);
    //supply.txt
    FILE* supply=fopen("supply.txt","r");
    if(supply==NULL)
    {
        printf("Can't open the file!\n");
        exit(1);
    }
    fscanf(supply,"AllSupplyLogs=%d\n",&AllSupplyLogs);
    for(int i=1;i<AllSupplyLogs+1;i++)
    {
        fscanf(supply,"{%d,%d,%d,%d,%d,{%d,%d,%d,%d},\"%[^\"]\"};\n",&Supplies[i].action,&Supplies[i].supply,&Supplies[i].number,&Supplies[i].user,&Supplies[i].approver,&Supplies[i].time.year,&Supplies[i].time.month,&Supplies[i].time.day,&Supplies[i].time.hour,Supplies[i].source);
    }
    fclose(supply);
    //config
    FILE* config=fopen("config.txt","r");
    if(config==NULL)
    {
        printf("Can't open the file!\n");
        exit(1);
    }
    fscanf(config,"CurrentUser=%d\n",&CurrentUser);
    fscanf(config,"AllGalaTickets=%d\n",&AllGalaTickets);
    fscanf(config,"AllVisitors=%d\n",&AllVisitors);
    fscanf(config,"%d %d %d %d %d \n",&sup[0],&sup[1],&sup[2],&sup[3],&sup[4]);
    fscanf(config,"Alnumivisitors=%d\n",&Alnumivisitors);
    fscanf(config,"Guestvisitors=%d\n",&Guestvisitors);
    fclose(config);
    return;
}
void LoginPage()//Login
{
    system(CLEAR);
    // Input the name and password
    char name[NAME_LENGTH];
    char password[PASSWORD_LENGTH];
    const char* name_notice="Please enter your name:(enter \"exit\" to exit，enter \"new\" to register)";
    InputControl(NAME_LENGTH,name,name_notice);
    if(strcmp(name,"exit")==0)
    {
        CurrentUser=8;
        return;
    }
    if(strcmp(name,"new")==0)
    {
        Register();
        return;
    }
    const char* password_notice="Please enter your password:";
    InputControl(PASSWORD_LENGTH,password,password_notice);
    //check if the name and password are correct
    system(CLEAR);
    for(int i=1;i<ALL_USERS+1;i++)
    {
        if(strcmp(name,Users[i].name)==0)
        {
            if(strcmp(password,Users[i].password)==0)
            {
                CurrentUser=i;
                if(Users[i].status==-1)
                {
                    CurrentUser=0;
                    printf("This user has been deleted\n");
                    PressEnterToContinue();
                    return;
                }
                printf("Login successfully!\n");
                printf("Welcome %s!\n\n",Users[i].name);
                PressEnterToContinue();
                return;
            }
            else
            {
                printf("Wrong name or wrong password!\n\n");
                PressEnterToContinue();
                return;
            }
        }
    }
    printf("Wrong name or wrong password!\n\n");
    PressEnterToContinue();
    return;
}
void Save()
{
    //save all the int data into config.txt
    FILE* id=fopen("config.txt","w");
    if(id==NULL)
    {
        printf("Can't open the file!\n");
        exit(1);
    }
    fprintf(id,"CurrentUser=0\n");
    fprintf(id,"AllGalaTickets=%d\n",AllGalaTickets);
    fprintf(id,"AllVisitors=%d\n",AllVisitors);
    fprintf(id,"%d %d %d %d %d \n",sup[0],sup[1],sup[2],sup[3],sup[4]);
    fprintf(id,"Alnumivisitors=%d\n",Alnumivisitors);
    fprintf(id,"Guestvisitors=%d\n",Guestvisitors);
    fclose(id);
    return;
}

void InputControl(const int INPUT_LENGTH,char* p,const char* q)//Input control
{
    do
    {
        system(CLEAR);
        printf("%s (the max length is %d)\n",q,INPUT_LENGTH-1);
        int input_have_enter=0;
        int flag1=-1;int flag2=-1;
        for(int i=0;i<INPUT_LENGTH;i++)
        {
            p[i]=getchar();
                if(p[i-1]!=' '&&p[i]==' ')
                {
                    flag1=i;
                    flag2=i;
                }
                if(p[i-1]==' '&&p[i]==' ')
                {
                    flag2=i;
                }
            if(p[i]=='\n')
            {
                p[i]='\0';
                input_have_enter=1;
                break;
            }
            else if(i==INPUT_LENGTH-1)
            {
                p[i]='\0';
                break;
            }
        }
        for(int i=0;i<INPUT_LENGTH;i++)
        {
            if(p[i]=='\0'&&flag2==i-1)
                p[flag1]='\0';
        }
        if(input_have_enter==0)
        {
            while(getchar()!='\n');
        }
    }while(p[0]=='\0');
}
void PrintFile(const char* filename,const char* notice)
{
    FILE* file=fopen(filename,"r");
    if(file==NULL)
    {
        printf("Can't open the file!\n");
        exit(1);
    }
    printf("%s\n",notice);
    char c;
    while(1)
    {
        c=fgetc(file);
        if(c==EOF)
        {
            break;
        }
        printf("%c",c);
    }
    fclose(file);
    printf("\n");
    return;
}
void PressEnterToContinue()//Press enter to continue
{
    printf("Press enter to continue...\n");
    while(getchar()!='\n');
    system(CLEAR);
    return;
}

void IDFileWrite()
{
    FILE* id=fopen("id.txt","w");
    if(id==NULL)
    {
        printf("Can't open the file!\n");
        exit(1);
    }
    fprintf(id,"CurrentUser=%d\n",AllUsers);
    for(int i=0;i<AllUsers+1;i++)
    {
        fprintf(id,"{%d,\"%s\",\"%s\"};\n",Users[i].status,Users[i].name,Users[i].password);
    }
    fclose(id);
    return;
}
void DonationFileWrite()
{
    FILE* donation=fopen("donation.txt","w");
    if(donation==NULL)
    {
        printf("Can't open the file!\n");
        exit(1);
    }
    fprintf(donation,"CurrentDonation=%d\n",AllDonations);
    for(int i=1;i<AllDonations+1;i++)
    {
        fprintf(donation,"{\"%s\",\"%s\",\"%s\",\"%s\",%d};\n",Donations[i].name,Donations[i].phone,Donations[i].donation,Donations[i].purpose,Donations[i].department);
    }
    fclose(donation);
    return;
}
void GalaTicketFileWrite()
{
    FILE* galactic_tickets=fopen("gala.txt","w");
    if(galactic_tickets==NULL)
    {
        printf("Can't open the file!\n");
        exit(1);
    }
    fprintf(galactic_tickets,"AllGalacticTicketsRequests=%d\n",AllGalacticTicketsRequests);
    for(int i=1;i<AllGalacticTicketsRequests+1;i++)
    {
        fprintf(galactic_tickets,"{%d,%d,%d};\n",GalacticTickets[i].user,GalacticTickets[i].status,GalacticTickets[i].ranum);
    }
    fclose(galactic_tickets);
    return;
}
void VisitorFileWrite()
{
    FILE* visiting=fopen("visiting.txt","w");
    if(visiting==NULL)
    {
        printf("Can't open the file!\n");
        exit(1);
    }
    fprintf(visiting,"AllVisitingRequests=%d\n",AllVisitingRequests);
    for(int i=1;i<AllVisitingRequests+1;i++)
    {
        fprintf(visiting,"{%d,%d,\"%s\",\"%s\",\"%s\",{%d,%d,%d}};\n",Visitors[i].user,Visitors[i].is_approved,Visitors[i].name,Visitors[i].phone,Visitors[i].purpose,Visitors[i].time.year,Visitors[i].time.month,Visitors[i].time.day);
    }
    fclose(visiting);
    return;
}
void ActivityFileWrite()
{
    FILE* activity=fopen("activities.txt","w");
    if(activity==NULL)
    {
        printf("Can't open the file!\n");
        exit(1);
    }
    fprintf(activity,"AllActivityRequests=%d\n",AllActivityRequests);
    for(int i=1;i<AllActivityRequests+1;i++)
    {
        fprintf(activity,"{%d,{%d",Activities[i].all_people,Activities[i].id[0]);
        for(int j=1;j<10;j++)
        {
            fprintf(activity,",%d",Activities[i].id[j]);
        }
        fprintf(activity,"},\"%s\",",Activities[i].group);
        fprintf(activity,"\"%s\",\"%s\",\"%s\",{%d,%d,%d,%d,%d,%d,%d},%d,{%d,%d,%d,%d,%d,%d,%d},%d,%d,%d};\n",Activities[i].name,Activities[i].place,Activities[i].content,Activities[i].activitytime.year,Activities[i].activitytime.month,Activities[i].activitytime.day,Activities[i].activitytime.start_day,Activities[i].activitytime.start_hour,Activities[i].activitytime.end_day,Activities[i].activitytime.end_hour,Activities[i].is_approvaed,Activities[i].approvaltime.year,Activities[i].approvaltime.month,Activities[i].approvaltime.day,Activities[i].approvaltime.start_day,Activities[i].approvaltime.start_hour,Activities[i].approvaltime.end_day,Activities[i].approvaltime.end_hour,Activities[i].approver,Activities[i].is_grant,Activities[i].grant);
    }
    fclose(activity);
    return;
}
void SupplyFileWrite()
{
    FILE* supply=fopen("supply.txt","w");
    if(supply==NULL)
    {
        printf("Can't open the file!\n");
        exit(1);
    }
    fprintf(supply,"AllSupplyLogs=%d\n",AllSupplyLogs);
    for(int i=1;i<AllSupplyLogs+1;i++)
    {
        fprintf(supply,"{%d,%d,%d,%d,%d,{%d,%d,%d,%d},\"%s\"};\n",Supplies[i].action,Supplies[i].supply,Supplies[i].number,Supplies[i].user,Supplies[i].approver,Supplies[i].time.year,Supplies[i].time.month,Supplies[i].time.day,Supplies[i].time.hour,Supplies[i].source);
    }
    fclose(supply);
    return;
}

void Register()
{
    system(CLEAR);
    // Input the name and password
    char name[NAME_LENGTH];
    const char* name_notice="Please enter your name:(enter \"exit\" to exit)";
    InputControl(NAME_LENGTH,name,name_notice);
    if(strcmp(name,"exit")==0)
    {
        return;
    }
    // Check if the name is used
    if(strcmp(name,"new")==0)
    {
        printf("The name is not able to use!\n");
        PressEnterToContinue();
        return;
    }
    for(int i=0;i<ALL_USERS;i++)
    {
        if(strcmp(name,Users[i].name)==0)
        {
            printf("The name is used!\n");
            PressEnterToContinue();
            return;
        }
    }
    char password[PASSWORD_LENGTH];
    const char* password_notice="Please enter your password:";
    InputControl(PASSWORD_LENGTH,password,password_notice);
    // Add the user
    AllUsers++;
    Users[AllUsers].status=7;
    strcpy(Users[AllUsers].name,name);
    strcpy(Users[AllUsers].password,password);
    // Write the file
    IDFileWrite();
    printf("Register successfully!\n");
    PressEnterToContinue();
    return;
}
void SupplyControl(int option)
{
    system(CLEAR);
    switch(option)
    {
        case 1:printf("Add the supply!\n");Supplies[AllSupplyLogs].action=1;break;
        case 2:printf("Request the supply!\n");Supplies[AllSupplyLogs].action=2;break;
    }
    AllSupplyLogs++;
    Supplies[AllSupplyLogs].action=option;
    // Input the name
    printf("Select the supply:\n");
    printf("1. Mask\n");
    printf("2. Bag\n");
    printf("3. Tag\n");
    printf("4. Notebook\n");
    int choice;
    do
    {
        printf("Please enter your choice:");
        choice=getchar()-'0';
    }while(choice<1||choice>4);
    while(getchar()!='\n');
    switch(choice)
    {
        case 1:Supplies[AllSupplyLogs].supply=1;break;
        case 2:Supplies[AllSupplyLogs].supply=2;break;
        case 3:Supplies[AllSupplyLogs].supply=3;break;
        case 4:Supplies[AllSupplyLogs].supply=4;break;
        default:break;
    }
    // Input the number
    printf("Please enter the number of the supply:");
    int number;int isavailable=1;
    do
    {
        isavailable=1;
        do
        {
            scanf("%d",&number);
        }while(number<=0);
        while(getchar()!='\n');
        Supplies[AllSupplyLogs].number=number;
        switch(option)
        {
            case 1:sup[choice]+=number;
                break;
            case 2:sup[choice]-=number;
                if(sup[choice]<0)
                {
                    printf("The supply is not enough!\n");
                    printf("Please enter the number of the supply:");
                    sup[choice]+=number;
                    isavailable=0;
                }
                break;
        }
    }while(isavailable==0);
    // Input the approver
    Supplies[AllSupplyLogs].user=0;
    Supplies[AllSupplyLogs].approver=CurrentUser;
    // Input the time
    do
    {
        system(CLEAR);
        printf("Please enter the time of the action:(yyyy mm dd hh)\n");
        printf("Year:");
        scanf("%d",&Supplies[AllSupplyLogs].time.year);
        printf("Month:");
        scanf("%d",&Supplies[AllSupplyLogs].time.month);
        printf("Day:");
        scanf("%d",&Supplies[AllSupplyLogs].time.day);
        printf("Hour:");
        scanf("%d",&Supplies[AllSupplyLogs].time.hour);
    }while(getchar()!='\n');
    // Input the source
    char source[SOURCE_LENGTH];
    const char* source_notice="Please enter the source of the supply:";
    switch(option)
    {
        case 1:
            InputControl(SOURCE_LENGTH,source,source_notice);
            strcpy(Supplies[AllSupplyLogs].source,source);
            break;
        case 2:
            int user;
            do
            {
                printf("Please enter the user id of the approver:");
                scanf("%d",&user);
            }while(user<1||user>AllUsers);
            while(getchar()!='\n');
            Supplies[AllSupplyLogs].user=user;
            strcpy(Supplies[AllSupplyLogs].source,"NULL");
            break;
        default:
            break;
    }
    SupplyFileWrite();
    printf("success!\n");
    PressEnterToContinue();
    return;
}

void AdminMenu()
{
    while(1)
    {
        int choice;
        do
        {
            system(CLEAR);
            printf("Welcome %s!\n\n",Users[CurrentUser].name);
            printf("Please choose the function you want to use:\n");
            printf("0. Exit\n");
            printf("1. Add a user\n");
            printf("2. Delete a user\n");
            choice=getchar()-'0';
        }while(choice<0||choice>2);
        while(getchar()!='\n');
        switch(choice)
        {
            case 0:CurrentUser=0;return;
            case 1:AddUser();break;
            case 2:DeleteUser();break;
            default:break;
        }
        Save();
    }
    return;
}
    void AddUser()
    {
        system(CLEAR);
        // Input the name and password
        char name[NAME_LENGTH];
        const char* name_notice="Please enter the name of the user:";
        InputControl(NAME_LENGTH,name,name_notice);
        if(strcmp(name,"exit")==0)
        {
            printf("Error!\n");
            return;
        }
        // Check if the name is used
        for (int i=1;i<AllUsers+1;i++)
        {
            if(strcmp(name,Users[i].name)==0)
            {
                printf("The name is used!\n");
                PressEnterToContinue();
                return;
            }
        }
        char password[PASSWORD_LENGTH];
        const char* password_notice="Please enter the password of the user:";
        InputControl(PASSWORD_LENGTH,password,password_notice);
        const char* status_notice="Please enter the status of the user:(1. Admin 2. Manager 3. Alumni 4. Teacher 5. Student 6. Workers 7. Guest)";
        int status;
        do
        {
            system(CLEAR);
            printf("%s\n",status_notice);
            status=getchar()-'0';
        }while(status<1||status>7);
        while(getchar()!='\n');
        // Add the user
        AllUsers++;
        Users[AllUsers].status=status;
        strcpy(Users[AllUsers].name,name);
        strcpy(Users[AllUsers].password,password);
        IDFileWrite();
        printf("Add user successfully!\n");
        PressEnterToContinue();
        return;
    }
    void DeleteUser()
    {
        system(CLEAR);
        // Input the name
        char name[NAME_LENGTH];
        const char* name_notice="Please enter the name of the user:(enter \"exit\" to exit))";
        InputControl(NAME_LENGTH,name,name_notice);
        if(strcmp(name,"exit")==0)
        {
            printf("Error!\n");
            return;
        }
        // Delete the user
        for(int i=1;i<AllUsers+1;i++)
        {
            if(strcmp(name,Users[i].name)==0)
            {
                Users[i].status=-1;
                IDFileWrite();
                printf("Delete user successfully!\n");
                PressEnterToContinue();
                return;
            }
        }
        printf("Can't find the user!\n");
        PressEnterToContinue();
        return;
    }
    void SetConfig()
    {
        while(1)
        {
            int choice;
            do
            {
                printf("Set the config\n");
                printf("0. Exit\n");
                printf("1. AllGalaTickets\n");
                printf("2. AllVisitors\n");
                printf("3. ALLalnumivisitors\n");
                printf("4. ALLGuestvisitors\n");
                printf("Please enter your choice:");
                choice=getchar()-'0';
            }while(choice<0||choice>4);
            while(getchar()!='\n');
            switch(choice)
            {
                case 0:return;
                case 1:
                    printf("Please enter the number of the tickets:");
                    scanf("%d",&AllGalaTickets);
                    while(getchar()!='\n');
                    break;
                case 2:
                    printf("Please enter the number of the visitors:");
                    scanf("%d",&AllVisitors);
                    while(getchar()!='\n');
                    break;
                case 3:
                    printf("Please enter the number of the alumni visitors:");
                    scanf("%d",&Alnumivisitors);
                    while(getchar()!='\n');
                    break;
                case 4:
                    printf("Please enter the number of the guest visitors:");
                    scanf("%d",&Guestvisitors);
                    while(getchar()!='\n');
                    break;
                default:break;
            }
            Save();
        }
    }
void ManagerMenu()
{
    while(1)
    {
        int choice;
        do
        {
            system(CLEAR);
            printf("Welcome %s!\n",Users[CurrentUser].name);
            printf("Please choose the function you want to use:\n");
            printf("0. Exit\n");
            printf("1. Add a visitor\n");
            printf("2. Approve the activity\n");
            printf("3. Approve the activity grant\n");
            printf("4. Approve the visitor\n");
            printf("5. Donation sort\n");
            printf("6. Donation List\n");
            printf("7. Gala ticket lottery\n");
            printf("8. Request supply\n");
            printf("9. Show log\n");
            printf("Please enter your choice:");
            choice=getchar()-'0';
        }while(choice<0||choice>9);
        while(getchar()!='\n');
        switch(choice)
        {
            case 0:CurrentUser=0;return;
            case 1:AddVisitor();break;
            case 2:ApproveActivity();break;
            case 3:ApproveActivityGrant();break;
            case 4:ApproveVisitor();break;
            case 5:DonationSort();break;
            case 6:DonationList();break;
            case 7:GalaTicketLottery();break;
            case 8:SupplyControl(2);break;
            case 9:ShowLog();break;
            default:break;
        }
        Save();
    }
    return;
}
    void AddVisitor()
    {
        system(CLEAR);
        // Input the name
        char name[NAME_LENGTH];
        const char* name_notice="Please enter the name of the visitor:(enter \"exit\" to exit))";
        InputControl(NAME_LENGTH,name,name_notice);
        if(strcmp(name,"exit")==0)
        {
            printf("Error!\n");
            return;
        }
        // Input the phone number
        char phone_number[PHONE_LENGTH];
        const char* phone_notice="Please enter the phone number of the visitor:";
        InputControl(PHONE_LENGTH,phone_number,phone_notice);

        // Input the reason
        char purpose[REASON_LENGTH];
        const char* reason_notice="Please enter the reason of the visitor:";
        InputControl(REASON_LENGTH,purpose,reason_notice);

        // Input the time
        int iscorrect=1;
        do
        {
            system(CLEAR);
            iscorrect=1;
            printf("Please enter the time of the visit:(yyyy mm dd)\n");
            scanf("%d %d %d",&Visitors[AllVisitingRequests].time.year,&Visitors[AllVisitingRequests].time.month,&Visitors[AllVisitingRequests].time.day);

            if(Visitors[AllVisitingRequests].time.year<2020||Visitors[AllVisitingRequests].time.month<1||Visitors[AllVisitingRequests].time.month>12||Visitors[AllVisitingRequests].time.day<1||Visitors[AllVisitingRequests].time.day>31)
            {
                iscorrect=0;
                printf("Error: Time incorrcet!\n");
                PressEnterToContinue();
            }
        }while(iscorrect==0);

        // Add the visitor
        Visitors[AllVisitingRequests].is_approved=2;
        strcpy(Visitors[AllVisitingRequests].name,name);
        strcpy(Visitors[AllVisitingRequests].phone,phone_number);
        strcpy(Visitors[AllVisitingRequests].purpose,purpose);

        AllVisitors--;
        AllVisitingRequests++;
        VisitorFileWrite();
        printf("Add visitor successfully!\n");
        return;
    }
    void ApproveActivity()
    {
        system(CLEAR);
        printf("Approve Activity!\n");
        // List all the activities status==1
        int waitingcount=0;
        for(int i=1;i<AllActivityRequests+1;i++)
        {
            if(Activities[i].is_approvaed==1)
            {
                waitingcount++;
            }
        }
        if(waitingcount==0)
        {
            printf("No activities waiting for approval!\n");
            PressEnterToContinue();
            return;
        }
        printf("The number of the activity waiting is %d\n",waitingcount);
        printf("The activities are:\n");
        printf("No.\tName\tPlace\tContent\tTime\n");
        for(int i=1;i<AllActivityRequests+1;i++)
        {
            if(Activities[i].is_approvaed==1)
            {
                printf("%d\t%s\t%s\t%s\t%d/%d/%d %d:00 - %d/%d/%d %d:00\n",i,Activities[i].name,Activities[i].place,Activities[i].content,Activities[i].activitytime.year,Activities[i].activitytime.month,Activities[i].activitytime.start_day,Activities[i].activitytime.start_hour,Activities[i].activitytime.year,Activities[i].activitytime.month,Activities[i].activitytime.end_day,Activities[i].activitytime.end_hour);
                int choice;
                do
                {
                    printf("Do you want to approve the activity?(y(es)/n(o)/q(uit))");
                    choice=getchar();
                }while(choice!='y'&&choice!='n'&&choice!='q');
                while(getchar()!='\n');
                if(choice=='y')
                {
                    Activities[i].is_approvaed=2;
                    Activities[i].approver=CurrentUser;
                    // input the approve time
                    printf("Please enter the approve time:\n");
                    printf("Year:");
                    scanf("%d",&Activities[i].approvaltime.year);
                    printf("Month:");
                    scanf("%d",&Activities[i].approvaltime.month);
                    printf("Day:");
                    scanf("%d",&Activities[i].approvaltime.day);
                    printf("Hour:");
                    scanf("%d",&Activities[i].approvaltime.hour);
                    ActivityFileWrite();
                    printf("Approve successfully!\n");
                }
                else if(choice=='n')
                {
                    Activities[i].is_approvaed=3;
                    Activities[i].approver=CurrentUser;
                    printf("Please enter the disapprove time:\n");
                    printf("Year:");
                    scanf("%d",&Activities[i].approvaltime.year);
                    printf("Month:");
                    scanf("%d",&Activities[i].approvaltime.month);
                    printf("Day:");
                    scanf("%d",&Activities[i].approvaltime.day);
                    printf("Hour:");
                    scanf("%d",&Activities[i].approvaltime.hour);
                    ActivityFileWrite();
                    printf("Disapprove successfully!\n");
                }
                else
                {
                    return;
                }
            }
        }
        printf("All the activities have been approved!\n");
        PressEnterToContinue();
        return;
    }
    void ApproveActivityGrant()
    {
        system(CLEAR);
        printf("Approve Activity Grant!\n");
        // List all the activities status==1
        int waitingcount=0;
        for(int i=1;i<AllActivityRequests+1;i++)
        {
            if(Activities[i].is_grant==1)
            {
                waitingcount++;
            }
        }
        if(waitingcount==0)
        {
            printf("No activities waiting for grant!\n");
            PressEnterToContinue();
            return;
        }
        printf("The number of the activity waiting is %d\n",waitingcount);
        printf("The activities are:\n");
        printf("No.\tName\tPlace\tContent\tTime\n");
        for(int i=1;i<AllActivityRequests+1;i++)
        {
            if(Activities[i].is_grant==1)
            {
                printf("%d\t%s\t%s\t%s\t%d/%d/%d\n",i,Activities[i].name,Activities[i].place,Activities[i].content,Activities[i].activitytime.year,Activities[i].activitytime.month,Activities[i].activitytime.day);
                printf("Do you want to grant the activity?(y(es)/n(o)/q(uit))");
                int choice;
                do
                {
                    choice=getchar();
                }while(choice!='y'&&choice!='n'&&choice!='q');
                while(getchar()!='\n');
                if(choice=='y')
                {
                    Activities[i].is_grant=2;
                    printf("Please enter the grant:");
                    scanf("%d",&Activities[i].grant);
                    while(getchar()!='\n');
                    ActivityFileWrite();
                    printf("Grant successfully!\n");
                }
                else if(choice=='n')
                {
                    Activities[i].is_grant=3;
                    ActivityFileWrite();
                    printf("Disgrant successfully!\n");
                }
                else
                {
                    return;
                }
            }
        }
    }
    void ApproveVisitor()
    {
        // List all the visitors status==1
        system(CLEAR);
        printf("The visitors waiting for approval:\n");
        int waitingcount=0;
        for(int i=1;i<AllVisitingRequests+1;i++)
        {
            if(Visitors[i].is_approved==1)
            {
                waitingcount++;
            }
        }
        if(waitingcount==0)
        {
            printf("No visitors waiting for approval!\n");
            PressEnterToContinue();
            return;
        }
        printf("The number of the visitor waiting is %d\n",waitingcount);
        printf("The visitors are:\n");
        printf("No.\tName\tPhone\t\t\tPurpose\t\t\t\t\tAlnumi/Guest\tAlnumi/ALL\tGuest/ALL\n");
        for(int i=1;i<AllVisitingRequests+1;i++)
        {
            if(Visitors[i].is_approved==1)
            {
                // check if the visitor is alnumi or guest
                int isalnumi=0;
                if(Visitors[i].user==3)
                {
                    isalnumi=1;
                }
                if(isalnumi==1)
                {
                    printf("%d\t%s\t%s\t\t%s\t\t\tAlnumi\t\t%d/%d\t\t%d/%d\n",i,Visitors[i].name,Visitors[i].phone,Visitors[i].purpose,Alnumivisitors,ALLalnumivisitors,Guestvisitors,ALLguestvisitors);
                }
                else
                {
                    printf("%d\t%s\t%s\t\t%s\t\t\tGuest\t\t%d/%d\t\t%d/%d\n",i,Visitors[i].name,Visitors[i].phone,Visitors[i].purpose,Alnumivisitors,ALLalnumivisitors,Guestvisitors,ALLguestvisitors);
                }
                printf("Do you want to approve the visitor?(y(es)/n(o)/q(uit))");
                int choice;
                do
                {
                    choice=getchar();
                }while(choice!='y'&&choice!='n'&&choice!='q');
                while(getchar()!='\n');
                if(choice=='y')
                {
                    Visitors[i].is_approved=2;
                    if(isalnumi==1)
                    {
                        Alnumivisitors++;
                    }
                    else
                    {
                        Guestvisitors++;
                    }
                    VisitorFileWrite();
                    printf("Approve successfully!\n");
                }
                else if(choice=='n')
                {
                    Visitors[i].is_approved=3;
                    VisitorFileWrite();
                    printf("Disapprove successfully!\n");
                }
                else
                {
                    return;
                }
            }
        }
        printf("All the visitors have been approved!\n");
        PressEnterToContinue();
        return;
    }
    void DonationSort()
    {
        //find the top10 donations
        system(CLEAR);
        //sort
        for(int i=1;i<AllDonations;i++)
        {
            for(int j=1;j<AllDonations-i+1;j++)
            {
                if(Donations[j].money<Donations[j+1].money)
                {
                    struct donation temp=Donations[j];
                    Donations[j]=Donations[j+1];
                    Donations[j+1]=temp;
                }
            }
        }
        printf("The top 10 donations are:\n");
        printf("No.\tName\tPhone\tDonation\tPurpose\tDepartment\n");
        for(int i=1;i<11;i++)
        {
            printf("%d\t%s\t%s\t%s\t%s\t%d\n",i,Donations[i].name,Donations[i].phone,Donations[i].donation,Donations[i].purpose,Donations[i].department);
        }
        PressEnterToContinue();
        return;
    }
    void DonationList()
    {
        while(1)
        {
            int choice;
            do
            {
                printf("Donation List\n");
                printf("Select the department:\n");
                PrintFile("department.txt","");
                printf("Y. All\n");
                printf("Z. Exit\n");
                printf("Please enter your choice:");
                choice=getchar();
                //choice [0-9;a-z;A-L]
            }while((choice>='0'&&choice<='9')||(choice>='a'&&choice<='z')||(choice>='A'&&choice<='L')||choice=='Y'||choice=='Z');
            if(choice=='Z')
            {
                return;
            }
            if(choice=='Y')
            {
                //list all the donations
                system(CLEAR);
                printf("All the donations are:\n");
                printf("No.\tName\tPhone\tDonation\tPurpose\tDepartment\n");
                for(int i=1;i<AllDonations+1;i++)
                {
                    printf("%d\t%s\t%s\t%s\t%s\t%d\n",i,Donations[i].name,Donations[i].phone,Donations[i].donation,Donations[i].purpose,Donations[i].department);
                }
                PressEnterToContinue();
                return;
            }
            // find the selected department
            system(CLEAR);
            printf("The donations of the department selected are:\n");
            printf("No.\tName\tPhone\tDonation\tPurpose\tDepartment\n");
            for(int i=1;i<AllDonations+1;i++)
            {
                if(Donations[i].department==choice)
                {
                    printf("%d\t%s\t%s\t%s\t%s\t%d\n",i,Donations[i].name,Donations[i].phone,Donations[i].donation,Donations[i].purpose,Donations[i].department);
                }
            }
            PressEnterToContinue();
            return;
            Save();
        }
    }
    void GalaTicketLottery()
    {
        system(CLEAR);
        printf("Gala Ticket Lottery!\n");
        printf("Enter the reserved tickets:");
        int reserved;
        scanf("%d",&reserved);
        while(getchar()!='\n');
        AllGalaTickets-=reserved;
        printf("Are you sure to start the lottery?(y(es)/n(o))");
        int choice;
        do
        {
            choice=getchar();
        }while(choice!='y'&&choice!='n');
        while(getchar()!='\n');
        if(choice=='n')
        {
            return;
        }
        // sort all the galatickets
        for(int i=1;i<AllGalacticTicketsRequests;i++)
        {
            for(int j=1;j<AllGalacticTicketsRequests-i+1;j++)
            {
                if(GalacticTickets[j].ranum<GalacticTickets[j+1].ranum)
                {
                    struct gala temp=GalacticTickets[j];
                    GalacticTickets[j]=GalacticTickets[j+1];
                    GalacticTickets[j+1]=temp;
                }
            }
        }
        // find the top 100 of the galatickets of each status and mark them as 2
        int count=0;
        int percent1;int count1=0;//alumni
        int percent2;int count2=0;//teachers
        int percent3;int count3=0;//students
        int percent4;int count4=0;//workers
        int percent5;int count5=0;//guests
        do
        {
            printf("Decide the percent of alnumi, teachers, students, workers and guests:\n");
            printf("Add up to 100. Each input must be intenger\n");
            printf("Enter the percent of the tickets for the alumni:");
            scanf("%d",&percent1);
            while(getchar()!='\n');
            printf("Enter the percent of the tickets for the teachers:");
            scanf("%d",&percent2);
            while(getchar()!='\n');
            printf("Enter the percent of the tickets for the students:");
            scanf("%d",&percent3);
            while(getchar()!='\n');
            printf("Enter the percent of the tickets for the workers:");
            scanf("%d",&percent4);
            while(getchar()!='\n');
            printf("Enter the percent of the tickets for the guests:");
            scanf("%d",&percent5);
            while(getchar()!='\n');
        }while(percent1+percent2+percent3+percent4+percent5!=100);
        percent1=percent1*AllGalaTickets/100;
        percent2=percent2*AllGalaTickets/100;
        percent3=percent3*AllGalaTickets/100;
        percent4=percent4*AllGalaTickets/100;
        percent5=percent5*AllGalaTickets/100;
        for(int i=1;i<AllGalacticTicketsRequests+1;i++)
        {
            if(GalacticTickets[i].status==1)
            {
                switch(Users[GalacticTickets[i].user].status)
                {
                    case 3:
                        if(count1<=percent1)
                        {
                            GalacticTickets[i].status=2;
                            count1++;count++;
                        }
                        break;
                    case 4:
                        if(count2<=percent2)
                        {
                            GalacticTickets[i].status=2;
                            count2++;count++;
                        }
                        break;
                    case 5:
                        if(count3<=percent3)
                        {
                            GalacticTickets[i].status=2;
                            count3++;count++;
                        }
                        break;
                    case 6:
                        if(count4<=percent4)
                        {
                            GalacticTickets[i].status=2;
                            count4++;count++;
                        }
                        break;
                    case 7:
                        if(count5<=percent5)
                        {
                            GalacticTickets[i].status=2;
                            count5++;count++;
                        }
                        break;
                    default:break;
                }
            }
            // disable all other tickets
            for(int i=1;i<AllGalacticTicketsRequests+1;i++)
            {
                if(GalacticTickets[i].status==1)
                {
                    GalacticTickets[i].status=3;
                }
            }
            if (count==AllGalaTickets)
            {
                printf("The lottery is over!\n");
                PressEnterToContinue();
                return;
            }
        }
        printf("The lottery is over! And there are tickets left.\n");
        GalaTicketFileWrite();
        PressEnterToContinue();
        return;
    }
    void RequestSupply()
    {
        system(CLEAR);
        printf("Request for the supply!\n");
        AllSupplyLogs++;
        Supplies[AllSupplyLogs].action=2;
        // Input the name
        printf("Select the supply:\n");
        printf("1. Mask\n");
        printf("2. Bag\n");
        printf("3. Tag\n");
        printf("4. Notebook\n");
        int choice;
        do
        {
            printf("Please enter your choice:");
            choice=getchar()-'0';
        }while(choice<1||choice>4);
        while(getchar()!='\n');
        switch(choice)
        {
            case 1:Supplies[AllSupplyLogs].supply=1;break;
            case 2:Supplies[AllSupplyLogs].supply=2;break;
            case 3:Supplies[AllSupplyLogs].supply=3;break;
            case 4:Supplies[AllSupplyLogs].supply=4;break;
            default:break;
        }
    }
    void ShowLog()
    {
        system(CLEAR);
        printf("Show the log of supply!\n");
        printf("0.Exit\n");
        printf("1.ShowAllLog\n");
        printf("2.ShowAddLog\n");
        printf("3.ShowRequestLog\n");
        printf("4.Cheak the number of the supply\n");
        int choice;
        do
        {
            printf("Please enter your choice:");
            choice=getchar()-'0';
        }while(choice<0||choice>4);
        while(getchar()!='\n');
        // print the log
        if(choice==0)
        {
            return;
        }
        if(choice==4)
        {
            //list all the supplies
            system(CLEAR);
            printf("The number of the supplies are:\n");
            printf("Mask\tBag\tTag\tNotebook\n");
            printf("%d\t%d\t%d\t%d\n",sup[1],sup[2],sup[3],sup[4]);
            PressEnterToContinue();
            return;
        }
        printf("Action:1.Add 2.Request\n");
        printf("Supply:1.Mask 2.Bag 3.Tag 4.Notebook\n");
        printf("No.\tAction\tSupply\tNumber\tUser\tApprover\tTime\tSource\n");
        for(int i=0;i<AllSupplyLogs+1;i++)
        {
            if(Supplies[i].action==1&&choice!=2)//add
            {
                printf("%d\t%d\t%d\t%d\tNone\t%d\t%d/%d/%d %d:00\t%s\n",i,Supplies[i].action,Supplies[i].supply,Supplies[i].number,Supplies[i].approver,Supplies[i].time.year,Supplies[i].time.month,Supplies[i].time.day,Supplies[i].time.hour,Supplies[i].source);
            }
            if(Supplies[i].action==2&&choice!=3)//request
            {
                printf("%d\t%d\t%d\t%d\t%d\t%d\t%d/%d/%d %d:00\tNone\n",i,Supplies[i].action,Supplies[i].supply,Supplies[i].number,Supplies[i].user,Supplies[i].approver,Supplies[i].time.year,Supplies[i].time.month,Supplies[i].time.day,Supplies[i].time.hour);
            }
        }
        PressEnterToContinue();
        return;
    }

void AlumniMenu()
{
    while(1)
    {
        int choice;
        do
        {
            system(CLEAR);
            printf("Welcome %s!\n\n",Users[CurrentUser].name);
            printf("Please choose the function you want to use:\n");
            printf("0. Exit\n");
            printf("1. Add the donation\n");
            printf("2. Cheak the Gala ticket\n");
            printf("3. Request the Gala ticket\n");
            printf("4. Request visiting\n");
            printf("5. Request supply\n");
            printf("Please enter your choice:");
            choice=getchar()-'0';
        }while(choice<0||choice>5);
        while(getchar()!='\n');
        switch(choice)
        {
            case 0:CurrentUser=0;return;
            case 1:AddDonation();break;
            case 2:CheakGalaTicket();break;
            case 3:RequestGalaTicket();break;
            case 4:RequestVisiting();break;
            case 5:SupplyControl(2);break;
            default:break;
        }
        Save();
    }
    return;
}
    void AddDonation()
    {
        system(CLEAR);
        // Input the name
        char name[NAME_LENGTH];
        const char* name_notice="Please enter your name :";
        InputControl(NAME_LENGTH,name,name_notice);
        // Input the phone number
        char phone_number[PHONE_LENGTH];
        const char* phone_notice="Please enter your phone number :";
        InputControl(PHONE_LENGTH,phone_number,phone_notice);
        // Input the donation
        char donation[DONATION_LENGTH];
        const char* donation_notice="Please enter your donation :";
        InputControl(DONATION_LENGTH,donation,donation_notice);
        // Input the purpose
        char purpose[PURPOSE_LENGTH];
        const char* purpose_notice="Please enter the purpose of your donation :";
        InputControl(PURPOSE_LENGTH,purpose,purpose_notice);
        // Input the department
        int department;
        const char* department_notice="Please enter the department of your donation :";
        do
        {
            system(CLEAR);
            PrintFile("department.txt","Here are the departments:");
            printf("%s\n",department_notice);
            department=getchar();
            //department [0-9,a-z,A-L]
        }while((department>='0'&&department<='9')||(department>='a'&&department<='z')||(department>='A'&&department<='L'));
        // Add the donation
        AllDonations++;
        strcpy(Donations[AllDonations].name,name);
        strcpy(Donations[AllDonations].phone,phone_number);
        strcpy(Donations[AllDonations].donation,donation);
        strcpy(Donations[AllDonations].purpose,purpose);
        Donations[AllDonations].department=department;
        DonationFileWrite();
        return;
    }
    void CheakGalaTicket()
    {
        system(CLEAR);
        int CurrentGalaTicket=-1;
        //find the ticket
        for(int i=1;i<AllGalacticTicketsRequests+1;i++)
        {
            if(GalacticTickets[i].user==CurrentUser)
            {
                CurrentGalaTicket=i;
                break;
            }
        }
        if(CurrentGalaTicket==-1)
        {
            printf("You haven't submit a request!\n");
            PressEnterToContinue();
            return;
        }
        printf("Here is the information of your Gala ticket:\n");
        //printf("Your ticket status is:%d\n",GalacticTickets[CurrentGalaTicket].status);
        switch(GalacticTickets[CurrentGalaTicket].status)
        {
            case 1:printf("Your request is waiting for lottery!\n");break;
            case 2:printf("Congraulations! You are in\n");break;
            case 3:printf("We are sorry that you don't have the ticket for the gala\n");break;
            default:break;
        }
        PressEnterToContinue();
    }
    void RequestGalaTicket()
    {
        system(CLEAR);
        printf("Request for the Gala ticket!\n");
        printf("Do you want to request for the Gala ticket?\n");
        printf("1. Yes\n");
        printf("2. Exit\n");
        int choice;
        do
        {
            printf("Please enter your choice:");
            choice=getchar();
        }while(choice!='1'&&choice!='2');
        while(getchar()!='\n');
        if(choice=='2')
        {
            return;
        }
        //cheak if the user has requested
        for(int i=1;i<AllGalacticTicketsRequests+1;i++)
        {
            if(GalacticTickets[i].user==CurrentUser)
            {
                printf("You have requested!\n");
                PressEnterToContinue();
                return;
            }
        }
        // Input the id
        AllGalacticTicketsRequests++;
        GalacticTickets[AllGalacticTicketsRequests].user=CurrentUser;
        GalacticTickets[AllGalacticTicketsRequests].status=1;
        // init the rand
        time_t t;
        srand((unsigned) time(&t));
        GalacticTickets[AllGalacticTicketsRequests].ranum=rand()%1000000;
        GalaTicketFileWrite();
        return;
    }
    void RequestVisiting()
    {
        system(CLEAR);
        printf("Request for entering the school!\n");
        // Input the name
        char name[NAME_LENGTH];
        const char* name_notice="Please enter your name :";
        InputControl(NAME_LENGTH,name,name_notice);
            //cheak if the user has requested
        for(int i=1;i<AllVisitingRequests+1;i++)
        {
            if(strcmp(Visitors[i].name,name)==0&&Visitors[i].is_approved!=0)
            {
                printf("You have requested! Now you need to submit again.\n");
                Visitors[i].is_approved=0;
                PressEnterToContinue();
                return;
            }
        }
        // Input the phone number
        char phone_number[PHONE_LENGTH];
        const char* phone_notice="Please enter your phone number :";
        InputControl(PHONE_LENGTH,phone_number,phone_notice);
        // Input the purpose
        char purpose[PURPOSE_LENGTH];
        const char* purpose_notice="Please enter the purpose of your visiting :";
        InputControl(PURPOSE_LENGTH,purpose,purpose_notice);
        // Input the time
        int year;
        int month;
        int day;
        const char* time_notice="Please enter the time of your visiting :\nthe format is yyyy mm dd\n";
        do
        {
            system(CLEAR);
            printf("%s\n",time_notice);
            scanf("%d",&year);
            scanf("%d",&month);
            scanf("%d",&day);
        }while(year<0||month<0||day<0||month>12||day>31);
        while(getchar()!='\n');
        // Storage
        AllVisitingRequests++;
        Visitors[AllVisitingRequests].user=CurrentUser;
        strcpy(Visitors[AllVisitingRequests].name,name);
        strcpy(Visitors[AllVisitingRequests].phone,phone_number);
        strcpy(Visitors[AllVisitingRequests].purpose,purpose);
        Visitors[AllVisitingRequests].time.year=year;
        Visitors[AllVisitingRequests].time.month=month;
        Visitors[AllVisitingRequests].time.day=day;
        Visitors[AllVisitingRequests].is_approved=1;
        VisitorFileWrite();
        printf("Your request has been sent!\n");
        return;
    }

void TeacherMenu()
{
    while(1)
    {
        int choice;
        do
        {
            system(CLEAR);
            printf("Welcome %s!\n\n",Users[CurrentUser].name);
            printf("Please choose the function you want to use:\n");
            printf("0. Exit\n");
            printf("1. Approve the activity grant\n");
            printf("2. Cheak the gala ticket\n");
            printf("3. Request the gala ticket\n");
            printf("Please enter your choice:");
            choice=getchar()-'0';
        }while(choice<0||choice>3);
        while(getchar()!='\n');
        switch(choice)
        {
            case 0:CurrentUser=0;return;
            case 1:ApproveActivityGrant();break;
            case 2:CheakGalaTicket();break;
            case 3:RequestGalaTicket();break;
            default:break;
        }
        Save();
    }
    return;
}

void StudentMenu()
{
    while(1)
    {
        int choice;
        do
        {
            system(CLEAR);
            printf("Welcome %s!\n\n",Users[CurrentUser].name);
            printf("Please choose the function you want to use:\n");
            printf("0. Exit\n");
            printf("1. Cheak the activity\n");
            printf("2. Cheak the gala ticket\n");
            printf("3. Request an activity\n");
            printf("4. Request the gala ticket\n");
            printf("Please enter your choice:");
            choice=getchar()-'0';
        }while(choice<0||choice>4);
        while(getchar()!='\n');
        switch(choice)
        {
            case 0:CurrentUser=0;return;
            case 1:CheakActivity();break;
            case 2:CheakGalaTicket();break;
            case 3:RequestActivity();break;
            case 4:RequestGalaTicket();break;
            default:break;
        }
        Save();
    }
    return;
}
    void CheakActivity()
    {
        system(CLEAR);
        printf("Here is the information of your activity:\n");
        //find the activity
        int CurrentActivity=-1;
        for(int i=1;i<AllActivityRequests+1;i++)
        {
            for(int j=0;j<10;j++)
            {
                if(Activities[i].id[j]==CurrentUser)
                {
                    CurrentActivity=i;
                    break;
                }
            }
        }
        if(CurrentActivity==-1)
        {
            printf("You haven't submit a request!\n");
            PressEnterToContinue();
            return;
        }
        switch(Activities[CurrentActivity].is_approvaed)
        {
            case 1:printf("Your request is waiting for approval!\n");break;
            case 2:printf("Your request has been approved!\n");break;
            case 3:printf("Your request has been disapproved!\n");break;
            default:break;
        }
        switch(Activities[CurrentActivity].is_grant)
        {
            case 1:printf("Your request is waiting for grant!\n");break;
            case 2:printf("Your request has been granted for %d !\n",Activities[CurrentActivity].grant);break;
            case 3:printf("Your request has been disgranted!\n");break;
            default:break;
        }
        PressEnterToContinue();
        return;
    }
    void RequestActivity()
    {
        system(CLEAR);
        printf("Request for the activity!\n");
        // Input the name
        printf("Select the owner of this activity:\n");
        printf("1. Single student\n");
        printf("2. Multiple student\n");
        printf("3. Student organization\n");
        AllActivityRequests++;
        int choice;
        do
        {
            printf("Please enter your choice:");
            scanf("%d",&choice);
        }while(choice<1||choice>3);
        while(getchar()!='\n');
        if(choice==1)
        {
            Activities[AllActivityRequests].all_people=1;
            Activities[AllActivityRequests].id[0]=CurrentUser;
            //set others to 0
            for(int i=1;i<=9;i++)
            {
                Activities[AllActivityRequests].id[i]=0;
            }
            strcpy(Activities[AllActivityRequests].group,"None");
        }
        else if(choice==2)
        {
            printf("Please enter the number of the students:");
            int number;
            scanf("%d",&number);
            Activities[AllActivityRequests].all_people=number;
            for(int i=0;i<number;i++)
            {
                printf("Please enter the id of the student:(%d/%d)",i+1,number);
                scanf("%d",&Activities[AllActivityRequests].id[i]);
            }
            //set others to 0
            for(int i=number+1;i<=9;i++)
            {
                Activities[AllActivityRequests].id[i]=0;
            }
            strcpy(Activities[AllActivityRequests].group,"None");
        }
        else if(choice==3)
        {
            Activities[AllActivityRequests].all_people=0;
            //set others to 0
            for(int i=0;i<=9;i++)
            {
                Activities[AllActivityRequests].id[i]=0;
            }
            char group[NAME_LENGTH];
            const char* name_notice="Please enter the name of your organization :";
            InputControl(NAME_LENGTH,group,name_notice);
        }
        //Input the activity name
        char activity_name[NAME_LENGTH];
        const char* activity_name_notice="Please enter the name of your activity :";
        InputControl(NAME_LENGTH,activity_name,activity_name_notice);
        // Input the activity place
        char activity_place[NAME_LENGTH];
        const char* activity_place_notice="Please enter the place of your activity :";
        InputControl(NAME_LENGTH,activity_place,activity_place_notice);
        // Input the activity content
        char activity_content[PURPOSE_LENGTH];
        const char* activity_content_notice="Please enter the content of your activity :";
        InputControl(PURPOSE_LENGTH,activity_content,activity_content_notice);
        // Input the time
        int year;
        int month;
        int day1;
        int hour1;
        int day2;
        int hour2;
        const char* time_notice="Please enter the time of your activity :\nthe format is yyyy mm (start)dd (start)hh (end)dd (end)hh\n";
        do
        {
            system(CLEAR);
            printf("%s\n",time_notice);
            scanf("%d",&year);
            scanf("%d",&month);
            // time start
            scanf("%d",&day1);
            scanf("%d",&hour1);
            // time end
            scanf("%d",&day2);
            scanf("%d",&hour2);
        }while(year<0||month<0||day1<0||day2<0||hour1<0||hour2<0||month>12||day1>31||day2>31||hour1>24||hour2>24);
        while(getchar()!='\n');
        //save
        strcpy(Activities[AllActivityRequests].name,activity_name);
        strcpy(Activities[AllActivityRequests].place,activity_place);
        strcpy(Activities[AllActivityRequests].content,activity_content);
        Activities[AllActivityRequests].activitytime.year=year;
        Activities[AllActivityRequests].activitytime.month=month;
        Activities[AllActivityRequests].activitytime.start_day=day1;
        Activities[AllActivityRequests].activitytime.start_hour=hour1;
        Activities[AllActivityRequests].activitytime.end_day=day2;
        Activities[AllActivityRequests].activitytime.end_hour=hour2;
        Activities[AllActivityRequests].is_approvaed=1;
        Activities[AllActivityRequests].is_grant=1;
        // Storage
        ActivityFileWrite();
        printf("Your request has been sent!\n");
        return;
    }

void WorkersMenu()
{
    while(1)
    {
        int choice;
        do
        {
            system(CLEAR);
            printf("Welcome %s!\n\n",Users[CurrentUser].name);
            printf("Please choose the function you want to use:\n");
            printf("0. Exit\n");
            printf("1. Cheak the visitor\n");
            printf("2. Cheak your gala ticket\n");
            printf("3. Request the gala ticket\n");
            printf("4. Add supply\n");
            printf("5. Request supply\n");
            printf("Please enter your choice:");
            choice=getchar()-'0';
        }while(choice<0||choice>5);
        while(getchar()!='\n');
        switch(choice)
        {
            case 0:CurrentUser=0;return;
            case 1:ApproveVisitorCheak();break;
            case 2:CheakGalaTicket();break;
            case 3:RequestGalaTicket();break;
            case 4:SupplyControl(1);break;
            case 5:SupplyControl(2);break;
            default:break;
        }
        Save();
    }
    return;
}
    void ApproveVisitorCheak()
    {
        system(CLEAR);
        printf("Approve the visitor cheak!\n");
        char name[NAME_LENGTH];
        const char* name_notice="Please enter the name of the visitor :";
        InputControl(NAME_LENGTH,name,name_notice);
        for(int i=1;i<=AllVisitingRequests;i++)
        {
            if(strcmp(Visitors[i].name,name)==0)
            {
                if(Visitors[i].is_approved==0)
                {
                    continue;
                }
                switch(Visitors[i].is_approved)
                {
                    case 1:printf("The visitor is waiting for approval!\n");break;
                    case 2:printf("The visitor has been approved!\n");break;
                    case 3:printf("The visitor has been disapproved!\n");break;
                    default:break;
                }
                PressEnterToContinue();
                return;
            }
        }
        printf("The visitor is not found!\n");
        return;
    }

void GuestMenu()
{
    while(1)
    {
        int choice;
        do
        {
            system(CLEAR);
            printf("Welcome %s!\n\n",Users[CurrentUser].name);
            printf("Please choose the function you want to use:\n");
            printf("0. Exit\n");
            printf("1. Cheak the gala ticket\n");
            printf("2. Cheak the visitor\n");
            printf("3. Request entering the school\n");
            printf("4. Request the gala ticket\n");
            printf("Please enter your choice:");
            choice=getchar()-'0';
        }while(choice<0||choice>4);
        while(getchar()!='\n');
        switch(choice)
        {
            case 0:CurrentUser=0;return;
            case 1:CheakGalaTicket();break;
            case 2:CheakVisiting();break;
            case 3:RequestVisiting();break;
            case 4:RequestGalaTicket();break;
            default:break;
        }
        Save();
    }
    return;
}
    void CheakVisiting()
    {
        system(CLEAR);
        //find the visitor
        int CurrentVisitor=-1;
        for(int i=1;i<AllVisitingRequests+1;i++)
        {
            if(Visitors[i].user==CurrentUser)
            {
                CurrentVisitor=i;
                if(Visitors[CurrentVisitor].is_approved==0)
                {
                    continue;
                }
                printf("Here is the information of your visiting:\n");
                switch(Visitors[CurrentVisitor].is_approved)
                {
                    case 1:printf("Your request is waiting for approval!\n");break;
                    case 2:printf("Your request has been approved!\n");break;
                    case 3:printf("Your request has been disapproved!\n");break;
                    default:break;
                }
                break;
            }
        }
        if(CurrentVisitor==-1)
        {
            printf("You haven't submit a request!\n");
            PressEnterToContinue();
            return;
        }
        PressEnterToContinue();
        return;
    }
