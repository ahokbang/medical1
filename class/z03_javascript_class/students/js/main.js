/*
1. ajax를 사용해서 stu_score.json 10개 데이터 출력 v
2. 학생입력 -> 학생추가 프로그램을 구성하시오.
3. 학생수정 -> 학생성적수정이 가능하게 구성하시오.
4. 학생삭제 -> 선택된 학생이 삭제되도록 구성하시오.
*/

$(function(){
    // 전역변수 선언
    let s_count = 1; 
    let o_id = 0;
    let o_no = 0;
    let o_name = "";
    let o_kor = 0;
    let o_eng = 0;
    let o_math = 0;

    // 1. 데이터 출력
    // 최초 데이터 불러오기
    $.ajax({
        url: "http://127.0.0.1:5500/students/json/stu_score.json",
        type: "get",
        data: {},
        dataType: "json",
        success:function(data){
            // alert("success")
            console.log(data);
            // s_count = data.length
            s_count = 10;
            let htmlData = "";
            for(let i=0; i<s_count; i++){
                htmlData += "<tr id='"+data[i].no+"'>";
                htmlData += "<td><input type='checkbox' name='stu' class='stuChk' value=''></td>";
                htmlData += '<td>'+data[i].no+'</td>';
                htmlData += '<td>'+data[i].name+'</td>';
                htmlData += '<td>'+data[i].kor+'</td>';
                htmlData += '<td>'+data[i].eng+'</td>';
                htmlData += '<td>'+data[i].math+'</td>';
                htmlData += '<td>'+data[i].total+'</td>';
                htmlData += '<td>'+data[i].avg+'</td>';
                htmlData += '<td>'+data[i].rank+'</td>';
                htmlData += "<td><button class='delBtn'>삭제</button></td>";
                htmlData += '</tr>';        
            } // for
            // html 소스 가져오기
            $("#tbody").html(htmlData);
        }, // success
        error:function(){
            alert("fail")
        } // error
    }); // ajax

    // 2. 학생입력
    // 2.1 학생입력버튼 클릭
    $("#writeBtn").click(function(){
        // alert("test");
        $(".p_all").css("display","block");
        // 학생성적수정폼을 같이 쓰게 되면서 이름 바뀜 ==> 학생성적입력으로 고정
        $(".p_main h2").text("학생성적입력");
        $("#name").prop("readonly",false);
    }); // 학생입력
    // 2.2 학생입력버튼>학생입력창>취소버튼
    $("#cancleBtn").click(function(){
        $(".p_all").css("display","none");
        // input 초기화
        $("#name").val("");
        $("#kor").val("");
        $("#eng").val("");
        $("#math").val("");
    }); // 학생입력버튼>학생입력창>취소버튼
    // 2.3 학생입력버튼>학생입력창>확인버튼(학생입력 내용 업데이트)
    $("#confirmBtn").click(function(){
        // 학생입력창을 수정하여 학생성적수정창을 열었으므로, 학생입력(수정)창의 확인버튼 id가 동일함.
        // input-hidden으로 id의 value 없는 경우는 입력창, 있는 경우는 수정창임을 확인할 수 있음.
        if($("#id").val()==""){ //$("#id").val()==""은 입력창
            console.log("이름 : "+$("#name").val());
            // 2.3.1 이름, 국어성적, 영어성적, 수학성적이 공백인 경우에도 표에 업데이트 되므로, 이름을 입력해야 등록 가능하게 설정
            if($("#name").val().length<2){
                alert("이름을 입력해주세요.");
                $("#name").focus();
                return false;
            } //if(("#name").val().length<2)

            s_count += 1;
            let i_name = $("#name").val();
            let i_kor = Number($("#kor").val());
            let i_eng = Number($("#eng").val());
            let i_math = Number($("#math").val());
            let i_total = i_kor+i_eng+i_math;
            let i_avg = (i_total/3).toFixed(1);
            
            // tr 추가
            let htmlData = "";
            htmlData += "<tr id='"+s_count+"'>";
            htmlData += "<td><input type='checkbox' name='stu' class='stuChk' value='"+s_count+"'></td>";
            htmlData += '<td>'+s_count+'</td>';
            htmlData += '<td>'+i_name+'</td>';
            htmlData += '<td>'+i_kor+'</td>';
            htmlData += '<td>'+i_eng+'</td>';
            htmlData += '<td>'+i_math+'</td>';
            htmlData += '<td>'+i_total+'</td>';
            htmlData += '<td>'+i_avg+'</td>';
            htmlData += '<td>0</td>';
            htmlData += "<td><button class='delBtn'>삭제</button></td>";
            htmlData += '</tr>';  
            // tbody에 추가
            $("#tbody").append(htmlData);
            // input 초기화
            $("#name").val("");
            $("#kor").val("");
            $("#eng").val("");
            $("#math").val("");
            $(".p_all").css("display","none");
        }else{ // ("#id").val() != ""은 수정창에 선택(체크)한 학생 정보가 있으므로 수정창을 의미
            // alert("학생성적수정창");

            o_no = $("#id").val();
            o_name = $("#name").val();
            o_kor = Number($("#kor").val());
            o_eng = Number($("#eng").val());
            o_math = Number($("#math").val());
            let o_total = o_kor+o_eng+o_math;
            let o_avg = (o_total/3).toFixed(1);

            let htmlData = "";
            htmlData += "<td><input type='checkbox' name='stu' class='stuChk' value='"+o_no+"'></td>";
            htmlData += '<td>'+o_no+'</td>';
            htmlData += '<td>'+o_name+'</td>';
            htmlData += '<td>'+o_kor+'</td>';
            htmlData += '<td>'+o_eng+'</td>';
            htmlData += '<td>'+o_math+'</td>';
            htmlData += '<td>'+o_total+'</td>';
            htmlData += '<td>'+o_avg+'</td>';
            htmlData += '<td>0</td>';
            htmlData += "<td><button class='delBtn'>삭제</button></td>";

            // html 소스 추가
            $("#"+o_no).html(htmlData);

            // 초기화
            $("#id").val("");
            $("#name").val("");
            $("#kor").val("");
            $("#eng").val("");
            $("#math").val("");
            $(".p_all").css("display","none");

        } // if/else(#id).val()==""
    }); // 학생입력버튼>학생입력창>확인버튼(학생입력 내용 업데이트)
    
    // 3. 학생수정 ==> 학생입력창의 확인/취소 버튼과 동일하므로 2. 학생입력에 관련 코드 추가
    // 3.1 학생수정 버튼 클릭 ==> 학생입력창 수정하여 사용
    $("#modifyBtn").click(function(){
        // alert("test");
        // 학생 선택하기 (1명)
        if($(".stuChk:checked").length!=1){
            alert("학생 1명을 선택해주세요");
            return false;
        } // if
        
        // 선택한(체크된) 학생정보 표시
        o_id = $(".stuChk:checked").parent();
        o_no = o_id.next().text();
        o_name = o_id.next().next().text();
        o_kor = o_id.next().next().next().text();
        o_eng = o_id.next().next().next().next().text();
        o_math = o_id.next().next().next().next().next().text();
        
        // 수정창 open
        $(".p_all").css("display","block");
        $("#name").prop("readonly",true);
        // 학생입력창 타이틀 수정 
        $(".p_main h2").text("학생성적수정");
        $("#id").val(o_no);
        $("#name").val(o_name);
        $("#kor").val(o_kor);
        $("#eng").val(o_eng);
        $("#math").val(o_math); 

    }); // 학생수정버튼 클릭


    // 4. 학생삭제
    // 4.1 table 삭제 버튼(.delBtn)으로 삭제하기
    $(document).on("click",".delBtn",function(){
        console.log("현재 선택된 class id : "+$(this).parent().parent().attr("id"));
        if(confirm("정말 삭제하시겠습니까?")){
            $("#"+$(this).parent().parent().attr("id")).remove();
        }
    }); // on("click",".delBtn",function()
    // 4.2 삭제할 학생 선택 해서 table 하단 삭제 버튼(#deleteBtn)으로 삭제하기
    // 4.2.1 머릿글 첫번째 열에 있는 체크박스 누르면 전체선택/다시 누르면(unchecked) 전체선택 해제
    $("#allChk").click(function(){
        if($(this).is(":checked") == true){
            // 전체선택
            $(".stuChk").each(function(){
                $(this).prop('checked', true);
            }); 
        }else{
            $(".stuChk").each(function(){
                $(this).prop('checked', false);
            });
        } // if/else($(this).is(":checked")==true)
    }); //$("#allChk").click(function()
    // 4.2.2 삭제할 학생 선택 및 table 하단 삭제 버튼(#deleteBtn)으로 삭제
    


}); // jquery