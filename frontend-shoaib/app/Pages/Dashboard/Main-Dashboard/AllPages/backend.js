class User {
    constructor(id, name, address, gender, email) {
        if (this.constructor === User) {
            throw new TypeError('Abstract class "User" cannot be directly constructed.');
        }

        this.id = id;
        this.name = name;
        this.address = address;
        this.gender = gender;
        this.email = email;
    }

    login() {
        console.log(`${this.name} has logged in.`);
    }
}

class Course {
    constructor(index, name, credit) {
        this.index=index;
        this.name = name;
        this.credit = credit;
    }
}

class Admin extends User {
    constructor(id, name, address, gender, email, password) {
        super(id, name, address, gender, email);
        this.password = password;
    }

    addFaculty(faculty) {
        University.addFac(faculty);
        //console.log(`Faculty ${faculty.name} has been added by ${this.name}`);
    }

    deleteFaculty(faculty) {
        University.removeFaculty(faculty);
        console.log(`Faculty ${faculty.name} has been deleted by ${this.name}`);
    }

    assignCourseToFaculty(course, faculty, timing) {
       University.offerCrs(faculty, course, timing); 
    }

  
    createCourse(courseName, courseCredit) {

        University.crsIndx +=1;
        const course = new Course(University.crsIndx, courseName, courseCredit);
        University.secNo[University.crsIndx]=0;
        University.courses.push(course);   
    }
}



class Faculty extends User {
  
    constructor(id, name, address, gender, email, department, password) {
        super(id, name, address, gender, email);
        this.department = department;
        this.assignedCourses = [];
        this.offerdCourses = [];
        this.password = password;
        this.creditcount =0;
    }
  

    offerCourse(sec) {
        this.offerdCourses.push(sec);
        //console.log(`Course ${course.name} is offered by ${this.name}`);
    }
}

class Room {
    constructor(number, available){
        this.number=number;
        this.available = available;
    }
}

class Section {
    constructor(course, number, time, room){
    this.course = course;
    this.number =number;
    this.time = time;
    this.room = room;    
    }

}

class Timing {
    constructor(startTime, endTime, day1, day2){
        this.startTime =startTime;
        this.endTime =endTime;
        this.day1 =day1;
        this.day2 =day2;
    }
}

class University {
    static faculties = [];
    static admins = [];
    static courses = [];
    static rooms = [];
    static secNo = [];
    static crsIndx = 0;
    

   static allocateRoom(){
    let room;
    this.rooms.map((e)=>e.available==true?room=e:null);
    return room;
   }

    constructor() {
    }


    static addsec(crs,timing){
        this.secNo[crs.index]+=1;
        const sec1 = new Section(crs,this.secNo[crs.index], timing, this.allocateRoom()) 
        return sec1;
    }

    static addAll(){
    this.faculties.push(new Faculty("100","abcshoaib","adsfd","234234","asdfdas","CSE","masai"));
    this.admins.push(new Admin("100","shoaib","adsfd","asdfdas","gmail","masai"));
    this.courses.push(new Course(0,"CSE102",'3'));
    this.secNo[0]=0;
    this.rooms.push(new Room(101,true))
    }

    static addFac(faculty){
    
     this.faculties.push(new Faculty(faculty.id, faculty.name, faculty.address, faculty.gender,
        faculty.email, faculty.department, faculty.password));
    }

    static createCrs(course){

        this.courses.unshift(course);
    }
    
    static removeFaculty(){
        
    }

    static offerCrs(fac, crs, timing){
    console.log(parseInt(fac.creditcount) + parseInt(crs.credit));
   // if(fac.creditcount + parseInt(crs.credit) <=11){
    fac.offerCourse(this.addsec(crs, timing));
    fac.creditcount += crs.credit;
   // }
  //  else {
        console.log("Error");
   // }
  }
}

export {University, Admin, Timing};