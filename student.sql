SET FOREIGN_KEY_CHECKS=0;
USE student;

-- ----------------------------
-- Table structure for `department`
-- ----------------------------
DROP TABLE IF EXISTS `department`;
CREATE TABLE `department` (
  `dname` char(50) NOT NULL,
  PRIMARY KEY (`dname`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
-- ----------------------------
-- Records of department
-- ----------------------------
INSERT INTO `department` VALUES ('计算机学院');
INSERT INTO `department` VALUES ('信息工程学院');
INSERT INTO `department` VALUES ('管理学院');
INSERT INTO `department` VALUES ('文学院');
INSERT INTO `department` VALUES ('理学院');


-- ----------------------------
-- Table structure for `major`
-- ----------------------------
DROP TABLE IF EXISTS `major`;
CREATE TABLE `major` (
  `mname` char(50) NOT NULL,
  `dname` char(20) NOT NULL,
  PRIMARY KEY (`mname`),
  FOREIGN KEY (`dname`) REFERENCES `department` (`dname`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
-- ----------------------------
-- Records of major
-- ----------------------------
INSERT INTO `major` VALUES ('计算机科学与技术', '计算机学院');
INSERT INTO `major` VALUES ('软件工程', '信息工程学院');
INSERT INTO `major` VALUES ('电子信息工程', '信息工程学院');
INSERT INTO `major` VALUES ('网络安全', '信息工程学院');
INSERT INTO `major` VALUES ('人工智能', '信息工程学院');


-- ----------------------------
-- Table structure for `class`
-- ----------------------------
DROP TABLE IF EXISTS `class`;
CREATE TABLE `class` (
  `class_id` char(20) NOT NULL,
  `mname` char(20) NOT NULL,
  PRIMARY KEY (`class_id`),
  FOREIGN KEY (`mname`) REFERENCES `major` (`mname`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
-- ----------------------------
-- Records of class
-- ----------------------------
INSERT INTO `class` VALUES ('21级计科1班', '计算机科学与技术');
INSERT INTO `class` VALUES ('21级计科2班', '计算机科学与技术');
INSERT INTO `class` VALUES ('21级网安1班', '网络安全');
INSERT INTO `class` VALUES ('21级网安2班', '网络安全');


-- ----------------------------
-- Table structure for `student`
-- ----------------------------
DROP TABLE IF EXISTS `student`;
CREATE TABLE `student` (
  sid char(20) NOT NULL,
  `sname` char(20) DEFAULT NULL,
  `gender` char(5) DEFAULT NULL,
  `age` char(5)  DEFAULT NULL,
  `class_id` char(20) NOT NULL,
  `photo` LONGBLOB DEFAULT NULL,
  PRIMARY KEY (`sid`),
  FOREIGN KEY (`class_id`) REFERENCES `class` (`class_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
-- ----------------------------
-- Records of student
-- ----------------------------
-- 学生数据初始化，学号、姓名、性别、班级号
INSERT INTO `student` VALUES ('S001', '张三', '男', '20', '21级计科1班', NULL);
INSERT INTO `student` VALUES ('S002', '李四', '男', '21', '21级计科1班', NULL);
INSERT INTO `student` VALUES ('S003', '王五', '女', '22', '21级计科2班', NULL);
INSERT INTO `student` VALUES ('S004', '赵六', '女', '21', '21级计科2班', NULL);
INSERT INTO `student` VALUES ('S005', '孙七', '男', '20', '21级网安1班', NULL);
INSERT INTO `student` VALUES ('S006', '周八', '女', '21', '21级网安2班', NULL);


-- ----------------------------
-- Table structure for `photo`
-- ----------------------------
-- DROP TABLE IF EXISTS `photo`;
-- CREATE TABLE `photo` (
--   `sid` char(20) NOT NULL,
--   `photo_data` LONGBLOB DEFAULT NULL,
--   FOREIGN KEY (`sid`) REFERENCES `student` (`sid`)
-- ) ENGINE=InnoDB DEFAULT CHARSET=utf8;
-- ----------------------------
-- Records of photo
-- ----------------------------


-- ----------------------------
-- Table structure for `course`
-- ----------------------------
DROP TABLE IF EXISTS `course`;
CREATE TABLE `course` (
  `cid` char(20) NOT NULL,
  `cname` char(50) DEFAULT NULL,
  `tid` char(20) NOT NULL,
  `credit` char(5) DEFAULT NULL,
  PRIMARY KEY (`cid`),
  FOREIGN KEY (`tid`) REFERENCES `teacher` (`tid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
-- ----------------------------
-- Records of course
-- ----------------------------
-- 课程数据初始化，课程号、课程名、教师号
INSERT INTO `course` VALUES ('C001', '数据库原理', 'T001', 4);
INSERT INTO `course` VALUES ('C002', '操作系统', 'T002', 2);
INSERT INTO `course` VALUES ('C003', '计算机网络', 'T003', 3);
INSERT INTO `course` VALUES ('C004', '数据结构', 'T004', 4);
INSERT INTO `course` VALUES ('C005', '算法分析', 'T005', 2);
INSERT INTO `course` VALUES ('C006', '人工智能', 'T006', 5);


-- ----------------------------
-- Table structure for `teacher`
-- ----------------------------
DROP TABLE IF EXISTS `teacher`;
CREATE TABLE `teacher` (
  `tid` char(20) NOT NULL,
  `tname` char(20) DEFAULT NULL,
  `gender` char(5) DEFAULT NULL,
  PRIMARY KEY (`tid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
-- ----------------------------
-- Records of teacher
-- ----------------------------
-- 老师数据初始化，教师号、姓名、性别
INSERT INTO `teacher` VALUES ('T001', '陈老师', '男');
INSERT INTO `teacher` VALUES ('T002', '林老师', '女');
INSERT INTO `teacher` VALUES ('T003', '张老师', '男');
INSERT INTO `teacher` VALUES ('T004', '李老师', '女');
INSERT INTO `teacher` VALUES ('T005', '王老师', '男');
INSERT INTO `teacher` VALUES ('T006', '赵老师', '女');


-- ----------------------------
-- Table structure for `grade`
-- ----------------------------
DROP TABLE IF EXISTS `grade`;
CREATE TABLE `grade` (
  `sid` char(20) NOT NULL,
  `cid` char(20) NOT NULL,
  `score` char(5) DEFAULT NULL,
  PRIMARY KEY (`sid`, `cid`),
  FOREIGN KEY (`sid`) REFERENCES `student` (`sid`),
  FOREIGN KEY (`cid`) REFERENCES `course` (`cid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
-- ----------------------------
-- Records of grade
-- ----------------------------
-- 成绩数据初始化，学号、课程号、成绩
INSERT INTO `grade` VALUES ('S001', 'C001', 85.00);
INSERT INTO `grade` VALUES ('S001', 'C002', 92.50);
INSERT INTO `grade` VALUES ('S001', 'C003', NULL);
INSERT INTO `grade` VALUES ('S001', 'C004', 92.50);
INSERT INTO `grade` VALUES ('S002', 'C001', 76.00);
INSERT INTO `grade` VALUES ('S002', 'C003', 88.00);
INSERT INTO `grade` VALUES ('S002', 'C005', 95.00);
INSERT INTO `grade` VALUES ('S002', 'C006', NULL);


-- ----------------------------
-- Table structure for `reward_punish`
-- ----------------------------
DROP TABLE IF EXISTS `reward_punish`;
CREATE TABLE `reward_punish` (
  `content` char(200) NOT NULL,
  `type` char(20) DEFAULT NULL,
  PRIMARY KEY (`content`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
-- ----------------------------
-- Records of reward_punish
-- ----------------------------
-- 奖惩数据初始化，内容、类型
INSERT INTO `reward_punish` VALUES ('优秀学生奖学金', '奖励');
INSERT INTO `reward_punish` VALUES ('英才班奖学金', '奖励');
INSERT INTO `reward_punish` VALUES ('学术竞赛一等奖', '奖励');
INSERT INTO `reward_punish` VALUES ('迟到', '惩罚');
INSERT INTO `reward_punish` VALUES ('旷课', '惩罚');
INSERT INTO `reward_punish` VALUES ('作弊', '惩罚'); 


-- ----------------------------
-- Table structure for `reward_punish_student`
-- ----------------------------
DROP TABLE IF EXISTS `reward_punish_student`;
CREATE TABLE `reward_punish_student` (
  `content` char(200) NOT NULL,
  `sid` char(20) NOT NULL,
  PRIMARY KEY (`content`, `sid`),
  FOREIGN KEY (`sid`) REFERENCES `student` (`sid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
-- ----------------------------
-- Records of reward_punish_student
-- ----------------------------
-- 奖惩_学生数据初始化，内容、学号
INSERT INTO `reward_punish_student` VALUES ('优秀学生奖学金', 'S001');
INSERT INTO `reward_punish_student` VALUES ('迟到', 'S001');
INSERT INTO `reward_punish_student` VALUES ('英才班奖学金', 'S002');
INSERT INTO `reward_punish_student` VALUES ('学术竞赛一等奖', 'S003');
INSERT INTO `reward_punish_student` VALUES ('迟到', 'S004');
INSERT INTO `reward_punish_student` VALUES ('旷课', 'S005');
INSERT INTO `reward_punish_student` VALUES ('作弊', 'S006');


-- ----------------------------
-- Table structure for `admin_login_k`
-- ----------------------------
DROP TABLE IF EXISTS `admin_login_k`;
CREATE TABLE `admin_login_k` (
  `admin_id` char(20) NOT NULL,
  `admin_pass` char(20) DEFAULT NULL,
  PRIMARY KEY (`admin_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
-- ----------------------------
-- Records of admin_login_k
-- ----------------------------
INSERT INTO `admin_login_k` VALUES ('admin', 'admin');


-- ----------------------------
-- Table structure for `stu_login_k`
-- ----------------------------
DROP TABLE IF EXISTS `stu_login_k`;
CREATE TABLE `stu_login_k` (
  `stu_id` char(20) NOT NULL,
  `stu_pass` char(20) DEFAULT NULL,
  PRIMARY KEY (`stu_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
-- ----------------------------
-- Records of stu_login_k
-- ----------------------------
INSERT INTO `stu_login_k` VALUES ('S001', '123456');
INSERT INTO `stu_login_k` VALUES ('S002', '123456');
INSERT INTO `stu_login_k` VALUES ('S003', '123456');
INSERT INTO `stu_login_k` VALUES ('S004', '123456');
INSERT INTO `stu_login_k` VALUES ('S005', '123456');
INSERT INTO `stu_login_k` VALUES ('S006', '123456');

DROP VIEW IF EXISTS BasicInfo;
CREATE VIEW BasicInfo AS
SELECT
  s.sid AS sid,
  s.sname AS sname,
  s.gender AS gender,
  s.age AS age,
  cl.class_id AS cid,
  m.mname AS mname,
  d.dname AS dname 
FROM
  student s
  JOIN class cl ON s.class_id = cl.class_id
  JOIN major m ON cl.mname = m.mname
  JOIN department d ON m.dname = d.dname;
 
DROP VIEW IF EXISTS ScoreInfo;
CREATE VIEW ScoreInfo AS
SELECT
  g.sid AS sid,
  g.cid AS cid,
  c.cname AS cname,
  t.tname AS tname,
  c.credit AS credit,
  g.score AS score
FROM
  grade g
  LEFT JOIN (course c JOIN teacher t ON c.tid = t.tid) ON g.cid = c.cid;

DROP VIEW IF EXISTS CourseInfo;
CREATE VIEW CourseInfo AS
SELECT
  c.cid AS cid,
  c.cname AS cname,
  t.tid AS tid,
  t.tname AS tname,
  c.credit AS credit
FROM
  course c JOIN teacher t ON c.tid = t.tid;

DROP VIEW IF EXISTS RewardInfo;
CREATE VIEW RewardInfo AS
SELECT
  s.sid AS sid,
  s.sname AS sname,
  rps.content AS content,
  rp.type AS type
FROM
  student s LEFT OUTER JOIN (reward_punish_student rps JOIN reward_punish rp ON rps.content = rp.content) ON s.sid = rps.sid;


DROP PROCEDURE IF EXISTS INSERT_STU;
DELIMITER //
CREATE PROCEDURE INSERT_STU(
    IN sid CHAR(20),
    IN sname CHAR(20),
    IN gender CHAR(5),
    IN age CHAR(5),
    IN clid CHAR(20),
    IN photo LONGBLOB
)
BEGIN
    DECLARE s INT DEFAULT 0;
    DECLARE cnt INT DEFAULT 0;
    START TRANSACTION;
    SELECT COUNT(*) FROM student s WHERE s.sid = sid INTO cnt;
    IF cnt = 0 THEN
      INSERT INTO student (sid, sname, gender, age, class_id, photo)
      VALUES (sid, sname, gender, age, clid, photo);
      COMMIT;
    ELSE
      ROLLBACK;
    END IF;
END //
DELIMITER ;


DROP PROCEDURE IF EXISTS INSERT_COU;
DELIMITER //
CREATE PROCEDURE INSERT_COU(
    IN cid CHAR(20),
    IN cname CHAR(50),
    IN tid CHAR(20),
    IN tname CHAR(5),
    IN credit CHAR(20)
)
BEGIN
    DECLARE s INT DEFAULT 0;
    DECLARE cnt INT DEFAULT 0;
    START TRANSACTION;
    SELECT COUNT(*) FROM course c WHERE c.cid = cid INTO cnt;
    IF cnt = 0 THEN
      INSERT INTO course (cid, cname, tid, credit)
      VALUES (cid, cname, tid, credit);
      COMMIT;
    ELSE
      ROLLBACK;
    END IF;
END //
DELIMITER ;


DROP PROCEDURE IF EXISTS INSERT_REW;
DELIMITER //
CREATE PROCEDURE INSERT_REW(
    IN sid CHAR(20),
    IN content CHAR(200)
)
BEGIN
    DECLARE s INT DEFAULT 0;
    DECLARE cnt INT DEFAULT 0;
    START TRANSACTION;
    SELECT COUNT(*) FROM reward_punish_student rps WHERE rps.sid = sid AND rps.content = content INTO cnt;
    IF cnt = 0 THEN
      INSERT INTO reward_punish_student (sid, content)
      VALUES (sid, content);
      COMMIT;
    ELSE
      ROLLBACK;
    END IF;
END //
DELIMITER ;


DROP PROCEDURE IF EXISTS INSERT_SCO;
DELIMITER //
CREATE PROCEDURE INSERT_SCO(
    IN sid CHAR(20),
    IN cid CHAR(20),
    IN score CHAR(5)
)
BEGIN
    DECLARE s INT DEFAULT 0;
    DECLARE cnt INT DEFAULT 0;
    START TRANSACTION;
    SELECT COUNT(*) FROM grade g WHERE g.sid = sid AND g.cid = cid INTO cnt;
    IF cnt = 0 THEN
      INSERT INTO grade (sid, cid, score)
      VALUES (sid, cid, score);
      COMMIT;
    ELSE
      ROLLBACK;
    END IF;
END //
DELIMITER ;


DROP PROCEDURE IF EXISTS UPDATE_STU;
DELIMITER //
CREATE PROCEDURE UPDATE_STU(
    IN sid CHAR(20),
    IN sname CHAR(20),
    IN gender CHAR(5),
    IN age CHAR(5),
    IN clid CHAR(20),
    IN photo LONGBLOB
)
BEGIN
    DECLARE s INT DEFAULT 0;
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET s = 1;
    START TRANSACTION;
    SELECT s.sid FROM student s WHERE s.sid = sid;
    IF s = 0 THEN
      UPDATE student s
      SET s.sname = sname, s.gender = gender, s.age = age, s.class_id = clid, s.photo = photo
      WHERE s.sid = sid;
      COMMIT;
    ELSE 
      ROLLBACK;
    END IF;
END //
DELIMITER ;


DROP PROCEDURE IF EXISTS UPDATE_COU;
DELIMITER //
CREATE PROCEDURE UPDATE_COU(
    IN cid CHAR(20),
    IN cname CHAR(50),
    IN tid CHAR(20),
    IN tname CHAR(5),
    IN credit CHAR(20)
)
BEGIN
    DECLARE s INT DEFAULT 0;
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET s = 1;
    START TRANSACTION;
    SELECT c.cid FROM course c WHERE c.cid = cid;
    SELECT t.tid FROM teacher t WHERE t.tid = tid;
    IF s = 0 THEN
      UPDATE course c
      SET c.cname = cname, c.tid = tid, c.credit = credit
      WHERE c.cid = cid;
      COMMIT;
    ELSE 
      ROLLBACK;
    END IF;
END //
DELIMITER ;


DROP PROCEDURE IF EXISTS UPDATE_SCO;
DELIMITER //
CREATE PROCEDURE UPDATE_SCO(
    IN sid CHAR(20),
    IN cid CHAR(20),
    IN score CHAR(5)
)
BEGIN
    DECLARE s INT DEFAULT 0;
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET s = 1;
    START TRANSACTION;
    SELECT c.cid FROM course c WHERE c.cid = cid;
    SELECT s.sid FROM student s WHERE s.sid = sid;
    IF s = 0 THEN
      UPDATE grade g
      SET g.sid = sid, g.cid = cid, g.score = score
      WHERE g.sid = sid AND g.cid = cid;
      COMMIT;
    ELSE 
      ROLLBACK;
    END IF;
END //
DELIMITER ;


DROP PROCEDURE IF EXISTS DELETE_STU;
DELIMITER //
CREATE PROCEDURE DELETE_STU(
    IN sid CHAR(20)
)
BEGIN
    DECLARE s INT DEFAULT 0;
    DECLARE cnt1 INT DEFAULT 0;
    DECLARE cnt2 INT DEFAULT 0;
    DECLARE cnt3 INT DEFAULT 0;
    DECLARE CONTINUE HANDLER FOR SQLEXCEPTION SET s = 1;
    START TRANSACTION;
    SET SQL_SAFE_UPDATES = 0;

    SELECT COUNT(*) FROM grade g WHERE g.sid = sid INTO cnt1;
    IF cnt1 > 0 THEN
      DELETE FROM grade g WHERE g.sid = sid;
    END IF;

    SELECT COUNT(*) FROM reward_punish_student rps WHERE rps.sid = sid INTO cnt2;
    IF cnt2 > 0 THEN
      DELETE FROM reward_punish_student rps WHERE rps.sid = sid;
    END IF;

    SELECT COUNT(*) FROM student s WHERE s.sid = sid INTO cnt3; 
    IF cnt3 > 0 THEN
      DELETE FROM student s WHERE s.sid = sid;
    END IF;

    IF s = 0 THEN
      COMMIT;
    ELSE 
      ROLLBACK;
    END IF;
    SET SQL_SAFE_UPDATES = 1;
END //
DELIMITER ;


DROP PROCEDURE IF EXISTS DELETE_COU;
DELIMITER //
CREATE PROCEDURE DELETE_COU(
    IN cid CHAR(20)
)
BEGIN
    DECLARE s INT DEFAULT 0;
    DECLARE cnt1 INT DEFAULT 0;
    DECLARE cnt2 INT DEFAULT 0;
    DECLARE CONTINUE HANDLER FOR SQLEXCEPTION SET s = 1;
    START TRANSACTION;
    SET SQL_SAFE_UPDATES = 0;

    SELECT COUNT(*) FROM grade g WHERE g.cid = cid INTO cnt1;
    IF cnt1 > 0 THEN
      DELETE FROM grade g WHERE g.cid = cid;
    END IF;

    SELECT COUNT(*) FROM course c WHERE c.cid = cid INTO cnt2; 
    IF cnt2 > 0 THEN
      DELETE FROM course c WHERE c.cid = cid;
    END IF;

    IF s = 0 THEN
      COMMIT;
    ELSE 
      ROLLBACK;
    END IF;
    SET SQL_SAFE_UPDATES = 1;
END //
DELIMITER ;


DROP PROCEDURE IF EXISTS DELETE_REW;
DELIMITER //
CREATE PROCEDURE DELETE_REW(
    IN sid CHAR(20),
    IN content CHAR(200)
)
BEGIN
    DECLARE s INT DEFAULT 0;
    DECLARE cnt1 INT DEFAULT 0;
    DECLARE CONTINUE HANDLER FOR SQLEXCEPTION SET s = 1;
    START TRANSACTION;
    SET SQL_SAFE_UPDATES = 0;

    SELECT COUNT(*) FROM reward_punish_student rps WHERE rps.sid = sid AND rps.content = content INTO cnt1;
    IF cnt1 > 0 THEN
      DELETE FROM reward_punish_student rps WHERE rps.sid = sid AND rps.content = content;
    END IF;

    IF s = 0 THEN
      COMMIT;
    ELSE 
      ROLLBACK;
    END IF;
    SET SQL_SAFE_UPDATES = 1;
END //
DELIMITER ;


DROP PROCEDURE IF EXISTS DELETE_SCO;
DELIMITER //
CREATE PROCEDURE DELETE_SCO(
    IN sid CHAR(20),
    IN cid CHAR(20)
)
BEGIN
    DECLARE s INT DEFAULT 0;
    DECLARE cnt1 INT DEFAULT 0;
    DECLARE CONTINUE HANDLER FOR SQLEXCEPTION SET s = 1;
    START TRANSACTION;
    SET SQL_SAFE_UPDATES = 0;

    SELECT COUNT(*) FROM grade g WHERE g.sid = sid AND g.cid = cid INTO cnt1;
    IF cnt1 > 0 THEN
      DELETE FROM grade g WHERE g.sid = sid AND g.cid = cid;
    END IF;

    IF s = 0 THEN
      COMMIT;
    ELSE 
      ROLLBACK;
    END IF;
    SET SQL_SAFE_UPDATES = 1;
END //
DELIMITER ;


DROP TRIGGER IF EXISTS AFTER_INSERT_student;
DELIMITER //
CREATE TRIGGER AFTER_INSERT_student AFTER INSERT ON student
FOR EACH ROW
BEGIN    
    INSERT INTO stu_login_k VALUES (NEW.sid, '123456');
END //
DELIMITER ;


DROP TRIGGER IF EXISTS AFTER_DELETE_student;
DELIMITER //
CREATE TRIGGER AFTER_DELETE_student AFTER DELETE ON student
FOR EACH ROW
BEGIN    
    DELETE FROM stu_login_k WHERE stu_id = OLD.sid;
END //
DELIMITER ;

Delimiter //
DROP FUNCTION IF EXISTS GPA;
CREATE FUNCTION GPA(sid CHAR(20))
RETURNS FLOAT
READS SQL DATA 
BEGIN
  DECLARE s, cnt INT DEFAULT 0;
  DECLARE grade, cred, total_c, total_g FLOAT DEFAULT 0;
  DECLARE sn1 VARCHAR(50);
  DECLARE c_count INT;
  DECLARE t, gpa FLOAT DEFAULT 0;
  DECLARE
    ct CURSOR FOR
    SELECT g.score, c.credit FROM grade g LEFT JOIN course c ON g.cid = c.cid WHERE g.sid = sid AND g.score IS NOT NULL;
  DECLARE CONTINUE HANDLER FOR NOT FOUND SET s = 1;
  SELECT COUNT(*) INTO cnt FROM grade g LEFT JOIN course c ON g.cid = c.cid WHERE g.sid = sid AND g.score IS NOT NULL;
  IF cnt != 0 THEN
  BEGIN
    OPEN ct;
    REPEAT
      FETCH ct INTO grade, cred;
      IF s = 0 THEN
        CASE 
          WHEN grade >= 95 THEN SET t = 4.3;
          WHEN grade >= 90 AND grade < 95 THEN SET t = 4.0;
          WHEN grade >= 85 AND grade < 90 THEN SET t = 3.7;
          WHEN grade >= 82 AND grade < 85 THEN SET t = 3.3;
          WHEN grade >= 78 AND grade < 82 THEN SET t = 3.0;
          WHEN grade >= 75 AND grade < 78 THEN SET t = 2.7;
          WHEN grade >= 72 AND grade < 75 THEN SET t = 2.3;
          WHEN grade >= 68 AND grade < 72 THEN SET t = 2.0;
          WHEN grade >= 65 AND grade < 68 THEN SET t = 1.7;
          WHEN grade = 64 THEN SET t = 1.5;
          WHEN grade >= 61 AND grade < 64 THEN SET t = 1.3;
          ELSE SET t = 1.0;
        END CASE;
        set total_g = total_g + t*cred;
        set total_c = total_c + cred;
      END IF;
    UNTIL s = 1
    END REPEAT;
    CLOSE ct;
    SET gpa = total_g / total_c;
  END;
  ELSE SET gpa = 0;
  END IF;
  RETURN gpa;
END //
Delimiter ;
