$(function(){
    let no = [1,2,3,4,5,6,7,8,9,10];
    let name = ['홍길동', '유관순', '이순신', '김구', '강감찬', '김유신', '홍길순', '홍길자', '최현묵', '이규원'];
    let kor = [62, 90, 64, 76, 51, 89, 77, 55, 73, 53];
    let eng = [70, 62, 73, 54, 55, 60, 67, 77, 51, 100];
    let math = [81, 79, 50, 83, 72, 79, 82, 86, 50, 94];
    let total = [213, 231, 187, 213, 178, 228, 226, 218, 174, 247];
    let avg = [71, 77, 62.3, 71, 59.3, 76, 75.3, 72.7, 58, 82.3];

    // tbody 부분 10개 행 생성
    let htmlData = "";
    for(let i=0;i<no.length; i++){
        htmlData += "<tr id='"+no[i]+"'>";
        htmlData += "<td><input type='checkbox' name='stu' class='stuChk' value='"+no[i]+"'></td>";
        htmlData += "<td>"+no[i]+"</td><td>"+name[i]+"</td><td>"+kor[i]+"</td>";
        htmlData += "<td>"+eng[i]+"</td><td>"+math[i]+"</td>";
        htmlData += "<td>"+total[i]+"</td><td>"+avg[i]+"</td><td>0</td>";
        htmlData += "<td><button class='delBtn'>삭제</button></td>";
        htmlData += "</tr>";
    } // for

    // html 소스를 tbody에 추가
    $("#tbody").html(htmlData);
    
    // 최초 실행 =======================================

        // 학생입력버튼 클릭
        $("#writeBtn").click(function(){
            // alert("test");
            $(".p_all").css("display","block");
        });

        $("#cancleBtn").click(function(){
            $(".p_all").css("display","none");
        });

    // 학생입력확인 버튼
    $("#confirmBtn").click(function(){
        // alert("test");
        // 글자- text() innerText, input-val() value, html() innerHtml
        console.log("이름 : "+$("#name").val());
        // console.log("국어점수 : "+$("#kor").val());
        // console.log("영어점수 : "+$("#eng").val());
        // console.log("수학점수 : "+$("#math").val());
        // console.log(Math.max.apply(null,no)+1); // 배열에서 최대값 구하기
        // apply() 메소드를 호출해서 함수 호출
        // no.push(Math.max.apply(null,no)+1); // 배열추가

        // 공백 확인
        if($("#name").val().length<2){  // 한글자 또는 아무글자가 없으면 안돼
            alert("이름을 입력하셔야 등록이 가능합니다.");
            $("#name").focus(); // focus() : 커서가 name에서 깜빡거려 
            return false;
        }
        
        let i_no = Math.max.apply(null,no)+1;
        no.push(i_no); // 나중에 db하면 번호생성은 자동으로 부여됨.
        let i_name = $("#name").val(); // type: string
        let i_kor = Number($("#kor").val()); // type: string 이므로 Number로 변환
        let i_eng = Number($("#eng").val());
        let i_math = Number($("#math").val());
        let i_total = i_kor+i_eng+i_math;
        let i_avg = (i_total/3).toFixed(2); //소수점2자리 반올림

        // table에 tr 추가
        let htmlData = "";        
        htmlData += "<tr id='"+i_no+"'>";
        htmlData += "<td><input type='checkbox' name='stu' class='stuChk' value='"+i_no+"'></td>";
        htmlData += "<td>"+i_no+"</td><td>"+i_name+"</td><td>"+i_kor+"</td>";
        htmlData += "<td>"+i_eng+"</td><td>"+i_math+"</td>";
        htmlData += "<td>"+i_total+"</td><td>"+i_avg+"</td><td>0</td>";
        htmlData += "<td><button class='delBtn'>삭제</button></td>";
        htmlData += "</tr>";
        
        // html 소스를 tbody에 추가
        // $("#tbody").html(htmlData); // html: 기존 html에 덮어쓰기
        // $("#tbody").prepend(htmlData); // prepend: 기존 html 위쪽에 추가, 게시글의 경우
        $("#tbody").append(htmlData); // append: 기존 html 아래쪽에 추가

        // input 초기화 ==> 확인을 누르면 빈공백이 계속 업데이트 돼
        $("#name").val("");
        $("#kor").val("");
        $("#eng").val("");
        $("#math").val(""); // val("안녕")이라고 쓰면 빈공백이 아닌 안녕이 남아
        $(".p_all").css("display","none"); // 학생입력창 사라지게 함

    }); //학생입력확인 버튼

    // 전체선택, 취소
    $("#allChk").click(function(){
        // alert("test");
        if($(this).is(":checked")==true){
            // 모든 체크박스 체크
            // console.log("체크되었습니다.");
            $(".stuChk").each(function(){
                $(this).prop("checked",true);
            });
        }else{
            // 모든 체크박스 언체크
            // console.log("체크 해제 되었습니다.");
            $(".stuChk").each(function(){
                $(this).prop("checked",false);
            });
        }
    });

    // table에 있는 삭제버튼 클릭
    $(document).on("click", ".delBtn", function(){       
        console.log("현재 선택된 class id: "+$(this).parent().parent().attr("id"));
        if(confirm("정말 삭제하시겠습니까?")){
            $("#"+$(this).parent().parent().attr("id")).remove(); // 새로 추가 입력한 데이터는 삭제되지 ㅇ낳아.
        }
    /*
    $(".delBtn").click(function(){
        console.log("현재 선택된 class id: "+$(this).parent().parent().attr("id"));
        if(confirm("정말 삭제하시겠습니까?")){
            $("#"+$(this).parent().parent().attr("id")).remove(); // 새로 추가 입력한 데이터는 삭제되지 ㅇ낳아.
        }
    */
    }); // table 삭제

    // 하단 삭제버튼 클릭
    $('#deleteBtn').click(function(){
        // alert("test");
        console.log("체크박스 개수 : "+$(".stuChk").length);
        // ********** 아래 두개는 같은 방법, 두 방법 모두 알아두기 ***********
        console.log("체크박스에서 체크된 개수 : "+$(".stuChk:checked").length);
        console.log("체크박스에서 체크된 개수 : "+$("input:checkbox[name='stu']:checked").length);
        // [name='stu']삭제가능하지만 여러개를 선택할 경우 작성해주어야 해.
        // console.log("체크박스에서 체크된 개수 : "+$("input:checkbox:checked").length);

        // 체크되어 있는 것이 없을 경우
        if($(".stuChk:checked").length<1){
            alert("삭제할 데이터를 체크해주셔야 가능합니다.");
            return false;
        }; // check if

        // 현재 체크박스가 체크가 되어 있는지 확인
        if(!confirm("정말 삭제하시겠습니까?")){ // ! 있으면 not
            return false; // yes 누르면 건너 뛰고, no 버튼 클릭 시 다시 돌아감
        }; // 삭제 if


        // 모든 체크박스를 가져오기
        $(".stuChk").each(function(){
            if($(this).is(":checked")==true){
                console.log("현재 선택된 class 값: "+$(this).val());
                console.log("현재 선택된 id 값 : "+$(this).parent().parent().attr("id"));
                $("#"+$(this).parent().parent().attr("id")).remove();
            }
        }); // each
    }); // 하단 삭제버튼


}); // 제이쿼리