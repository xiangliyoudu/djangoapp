$(function(){  
	//动态加载所属平台列表
	$.ajax({
		type:"GET",//请求类型
		url:"/dev/datadictionarylist.json",//请求的url
		data:{tcode:"APP_FLATFORM"},//请求参数
		dataType:"json",//ajax接口（请求url）返回的数据类型
		success:function(data){//data：返回数据（json对象）
		    data = JSON.parse(data)
			$("#flatformId").html("");
			var options = "<option value=\"\">--请选择--</option>";
			for(var i = 0; i < data.length; i++){
				options += "<option value=\""+data[i].fields.valueid+"\">"+data[i].fields.valuename+"</option>";
			}
			$("#flatformId").html(options);
		},
		error:function(data){//当访问时候，404，500 等非200的错误状态码
			alert("加载平台列表失败！");
		}
	});  
	//动态加载一级分类列表
	$.ajax({
		type:"GET",//请求类型
		url:"/backend/categorylevellist.json/",//请求的url
		data:{pid: null},//请求参数
		dataType:"json",//ajax接口（请求url）返回的数据类型
		success:function(data){//data：返回数据（json对象）
		    field = JSON.parse(data)
			$("#categoryLevel1").html("");
			var options = "<option value=\"\">--请选择--</option>";
			for(var i = 0; i < field.length; i++){
				options += "<option value=\""+field[i].pk+"\">"+field[i].fields.categoryname+"</option>";
			}
			$("#categoryLevel1").html(options);
		},
		error:function(data){//当访问时候，404，500 等非200的错误状态码
			alert("加载一级分类列表失败！");
		}
	});  
	//动态加载二级分类列表
	$("#categoryLevel1").change(function(){
		var categoryLevel1 = $("#categoryLevel1").val();
		if(categoryLevel1 != '' && categoryLevel1 != null){
			$.ajax({
				type:"GET",//请求类型
				url:"/backend/categorylevellist.json/",//请求的url
				data:{pid:categoryLevel1},//请求参数
				dataType:"json",//ajax接口（请求url）返回的数据类型
				success:function(data){//data：返回数据（json对象）
				    field = JSON.parse(data)
					$("#categoryLevel2").html("");
					var options = "<option value=\"\">--请选择--</option>";
					for(var i = 0; i < field.length; i++){
						options += "<option value=\""+field[i].pk +"\">"+field[i].fields.categoryname+"</option>";
					}
					$("#categoryLevel2").html(options);
				},
				error:function(data){//当访问时候，404，500 等非200的错误状态码
					alert("加载二级分类失败！");
				}
			});
		}else{
			$("#categoryLevel2").html("");
			var options = "<option value=\"\">--请选择--</option>";
			$("#categoryLevel2").html(options);
		}
		$("#categoryLevel3").html("");
		var options = "<option value=\"\">--请选择--</option>";
		$("#categoryLevel3").html(options);
	});
	//动态加载三级分类列表
	$("#categoryLevel2").change(function(){
		var categoryLevel2 = $("#categoryLevel2").val();
		if(categoryLevel2 != '' && categoryLevel2 != null){
			$.ajax({
				type:"GET",//请求类型
				url:"/backend/categorylevellist.json/",//请求的url
				data:{pid:categoryLevel2},//请求参数
				dataType:"json",//ajax接口（请求url）返回的数据类型
				success:function(data){//data：返回数据（json对象）
					field = JSON.parse(data)
					$("#categoryLevel3").html("");
					var options = "<option value=\"\">--请选择--</option>";
					for(var i = 0; i < field.length; i++){
						options += "<option value=\""+field[i].pk+"\">"+field[i].fields.categoryname+"</option>";
					}
					$("#categoryLevel3").html(options);
				},
				error:function(data){//当访问时候，404，500 等非200的错误状态码
					alert("加载三级分类失败！");
				}
			});
		}else{
			$("#categoryLevel3").html("");
			var options = "<option value=\"\">--请选择--</option>";
			$("#categoryLevel3").html(options);
		}
	});
	
	$("#back").on("click",function(){
		window.location.href = "../";
	});
	
	$("#APKName").bind("blur",function(){
		//ajax后台验证--APKName是否已存在
		$.ajax({
			type:"GET",//请求类型
			url:"/dev/apkexist.json/",//请求的url
			data:{APKName:$("#APKName").val()},//请求参数
			dataType:"json",//ajax接口（请求url）返回的数据类型
			success:function(data){//data：返回数据（json对象）
				if(data == "empty"){//参数APKName为空，错误提示
					alert("APKName为不能为空！");
				}else if(data == "exist"){//账号不可用，错误提示
					alert("该APKName已存在，不能使用！");
				}else if(data == "noexist"){//账号可用，正确提示
					alert("该APKName可以使用！");
				}
			},
			error:function(data){//当访问时候，404，500 等非200的错误状态码
				alert("请求错误！");
			}
		});
	});

});
      
      
      