public class CutomizedClass {
    String name;
    String phone;
    String mail;
    String address;
    public CutomizedClass(String name,String phone,String mail,String address) {
        this.name = name;
        this.phone = phone;
        this.mail = mail;
        this.address = address;
    }
    public void printmessage(){
        System.out.println(name+phone+mail+address);
    }

    public static void main(String[] args) {
        // write your code here

        CutomizedClass p1 = new CutomizedClass("John", "123", "abc@abc", "taipei");
        p1.printmessage();
    }
}
