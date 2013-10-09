Feature: Policy Create

@policy
@policy_create
Scenario: Goal 1 : Click Menu policy
Given Admin login to backoffice
When เมื่อคลิกปุ่ม [เพิ่ม Policy]
Then หน้าจอ [Add Policy] ต้องแสดงได้ถูกต้อง
And ต้องมีฟิลด์ policy type
And ต้องมีฟิลด์ name
And ต้องมีฟิลด์ shot desc
And ต้องมีฟิลด์ description
And ต้องมีฟิลด์ logo
And ต้องมีฟิลด์ status
And ต้องมีฟิลด์ ปุ่ม save
And ต้องมีฟิลด์ ปุ่ม reset
When Admin click policy type option
Then Drop Down list จะแสดงครบทุก type (คืนของ, คืนเงิน, ส่งสินค้า)

@policy
@policy_create
Scenario: Goal 2 : Save data
Given Admin อยู่ที่หน้า add Policy
When Admin กรอกข้อมูลครบทุกฟิลด์
And Admin click ปุ่ม Save
Then หน้าเว็บจะ redirect ไปหน้า policy list
And ที่ policy list จะต้องมีข้อมูลที่ add ครบถ้วน
And ในDB ต้องมีข้อมูลที่กรอกไปครบถ้วน
And File รูปต้องเก็บไว้ที่ NAS ได้ถูกต้อง

@policy
@policy_create
Scenario: Goal 3 : Validate field 
Given Admin อยู่ที่หน้า add Policy
When Admin click save button
Then Show error message "กรุณากรอก Policy type"
Then Show error message "กรุณากรอก Name"
Then Show error message "กรุณากรอก Shot desc"
Then Show error message "กรุณากรอก Desc"
Then Show error message "กรุณากรอก Logo"

@policy
@policy_create
Scenario: Goal 4 : ValidatelLogo size
Given Admin อยู่ที่หน้า add Policy
When Admin upload รูปเกิน max size xxx
Then Show error message

@policy
@policy_create
Scenario: Goal 5 : Validate logo extension นามสกุลไฟล์
Given Admin อยู่ที่หน้า add Policy
When Admin upload ไฟล์ผิด type
Then จะ show error message

@policy
@policy_create
Scenario: Goal 6 : Validate logo resolution
Given Admin อยู่ที่หน้า add Policy
When Admin upload รูปที่เกินขนาด W x H
Then จะ show error message




























