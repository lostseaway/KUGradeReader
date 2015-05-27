<?php
$to = "tlostseaway@gmail.com";
$subject = $_POST['subject']." : KUGradeReader Alert!!";
$txt = $_POST['subject']." : ".$_POST['grade'];
$headers = "From: wm@example.com";

mail($to,$subject,$txt,$headers);
?>
