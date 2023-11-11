public class Gender {
    public static void main(String[] args) {
        if (args.length != 2) {
            System.out.println("Usage: java InterestCalculator <Gender> <Age>");
            return;
        }

        String gender = args[0].toLowerCase();
        int age = Integer.parseInt(args[1]);

        double interestRate = 0.0;

        if (gender.equals("female")) {
            if (age >= 1 && age <= 58) {
                interestRate = 8.2;
            } else if (age >= 59 && age <= 120) {
                interestRate = 7.6;
            }
        } else if (gender.equals("male")) {
            if (age >= 1 && age <= 60) {
                interestRate = 9.2;
            } else if (age >= 61 && age <= 120) {
                interestRate = 8.3;
            }
        } else {
            System.out.println("Invalid gender. Please specify 'Male' or 'Female'.");
            return;
        }

        if (interestRate == 0.0) {
            System.out.println("Invalid age. Please specify an age between 1 and 120.");
            return;
        }

        System.out.println("Interest Rate: " + interestRate + "%");
    }
}