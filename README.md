# MyMovieRecommendSystem

#### 죽기 전에 꼭 봐야 할 영화

#### 많은 사람들로부터 인정 받은 영화

#### 흥행에 성공한 영화

![image-20210513220645207](README.assets/image-20210513220645207.png)

### 아카데미상 유형

**ACTOR IN A LEADING ROLE(남우주연상)**

**ACTOR IN A SUPPORTING ROLE(남우조연상)**

**ACTRESS IN A LEADING ROLE(여우주연상)**

**ACTRESS IN A SUPPORTING ROLE(여우조연상)**

​	후보 구분자 class : actingorsimilar

​	*nominationstatement*(배우이름)--*film*{"*charactor*"}

**ANIMATED FEATURE FILM(장편애니메이션상)**

​	후보 구분자 class : other

​	*film*--*nominationstatement*(제작자들이름)

**CINEMATOGRAPHY(촬영상)**

​	후보 구분자 class : actingorsimilar

​	*film*--*nominationstatement*(촬영감독이름)

**COSTUME DESIGN(의상상)**

​	후보 구분자 class : actingorsimilar

​	*film*--*nominationstatement*(의상감독이름)

**DIRECTING(감독상)**

​	후보 구분자 class : actingorsimilar

​	*film*--*nominationstatement*(감독이름)

**DOCUMENTARY (Feature)(장편다큐멘터리상)**

​	후보 구분자 class : actingorsimilar

​	*film*--*nominationstatement*(제작자들이름)

**DOCUMENTARY (Short Subject)(단편다큐멘터리상)**

​	후보 구분자 class : actingorsimilar

​	*film*--*nominationstatement*(제작자들이름)

**FILM EDITING(편집상)**

​	후보 구분자 class : actingorsimilar

​	*film*--*nominationstatement*(편집감독이름)

**INTERNATIONAL FEATURE FILM(국제영화상)**

​	후보 구분자 class : other

​	*film*--*nominationstatement*(나라)

**MAKEUP AND HAIRSTYLING(분장상)**

​	후보 구분자 class : other

​	*film*--*nominationstatement*(여러명이름)

**MUSIC (Original Score)(음악상)**

​	후보 구분자 class : other

​	*film*--*nominationstatement*

**MUSIC (Original Song)(주제가상)**

​	후보 구분자 class : song

​	"*songtitle*" from	*film*--*nominationstatement*(Music by 작곡가;Lyric by 작사가)

**BEST PICTURE(작품상)**

​	후보 구분자 class : actingorsimilar

​	*film*--*nominationstatement*(제작자들 이름)

**PRODUCTION DESIGN(미술상)**

​	후보 구분자 class : other

​	*film*--*nominationstatement*(Production Design:사람이름, Set Decoration:사람이름)

**SHORT FILM (Animated)(단편애니메이션상)**

​	후보 구분자 class : other

​	*film*--*nominationstatement*(제작자들이름)

**SHORT FILM (Live Action)(단편영화상)**

​	후보 구분자 class : other

​	*film*--*nominationstatement*(제작자들이름)

**SOUND(음향상)**

​	후보 구분자 class : other

​	*film*--*nominationstatement*(제작자들이름)

**VISUAL EFFECTS(시각효과상)**

​	후보 구분자 class : actingorsimilar

​	*film*--*nominationstatement*(제작자들이름)

**WRITING (Adapted Screenplay)(각색상)**

​	후보 구분자 class : actingorsimilar

​	*film*--*nominationstatement*(제작자들이름)

**WRITING (Original Screenplay)(각본상)**

​	후보 구분자 class : actingorsimilar

​	*film*--*nominationstatement*(제작자들이름)

**JEAN HERSHOLT HUMANITARIAN AWARD(진 허숄트 )**

​	후보 구분자 class : honorary

​	*nominationstatement*



































































