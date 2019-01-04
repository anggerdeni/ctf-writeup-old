<?php
	include "header.php";
?>

<body>
	
	<div class="limiter">
		<div class="container-login100">
			<div class="wrap-login100">
				<form class="login100-form validate-form" method="POST" action="login_proc.php">
					<span class="login100-form-title p-b-34">
						Hibiki Command Panel
					</span>
					
					<div class="wrap-input100 rs1-wrap-input100 validate-input m-b-20" data-validate="Type user name">
						<input id="first-name" class="input100" type="text" name="username" placeholder="User name">
						<span class="focus-input100"></span>
					</div>
					<div class="wrap-input100 rs2-wrap-input100 validate-input m-b-20" data-validate="Type password">
						<input class="input100" type="password" name="password" placeholder="Password">
						<span class="focus-input100"></span>
					</div>

					
					<div class="container-login100-form-btn">
						<button class="login100-form-btn">
							Masuk
						</button>
					</div>

					<div class="w-full text-center"><br>
						Belum punya akun? 
						<a href="register.php" class="txt3">
							Daftar
						</a>
					</div>
				</form>

				<div class="login100-more" style="background-image: url('https://i.pinimg.com/originals/6d/fb/35/6dfb35287538bd1723dd6b3f786082ce.jpg');"></div>
			</div>
		</div>
	</div>
	
	

	<div id="dropDownSelect1"></div>
<?php
	include "footer.php";
?>
