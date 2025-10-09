import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.Statement;

public class MinhaApp {
    public static void main(String[] args) {
        // Conexão com o banco via variáveis de ambiente
        String url = "jdbc:mysql://" + System.getenv("DB_HOST") + ":" + System.getenv("DB_PORT") + "/" + System.getenv("DB_NAME");
        String user = System.getenv("DB_USER");
        String password = System.getenv("DB_PASS");

        // Tipos de usuário definidos no Dockerfile
        String tipoAdmin = System.getenv("USER_ADMIN");
        String tipoCliente = System.getenv("USER_CLIENTE");
        String tipoCorretor = System.getenv("USER_CORRETOR");

        try {
            Class.forName("com.mysql.cj.jdbc.Driver");
            Connection conn = DriverManager.getConnection(url, user, password);
            Statement stmt = conn.createStatement();

            System.out.println("=== Usuários ADMIN ===");
            ResultSet rsAdmin = stmt.executeQuery("SELECT nome, email FROM Usuario WHERE tipo_usuario='" + tipoAdmin + "'");
            while(rsAdmin.next()){
                System.out.println("Nome: " + rsAdmin.getString("nome") + ", Email: " + rsAdmin.getString("email"));
            }
            rsAdmin.close();

            System.out.println("\n=== Usuários CLIENTE ===");
            ResultSet rsCliente = stmt.executeQuery("SELECT nome, email FROM Usuario WHERE tipo_usuario='" + tipoCliente + "'");
            while(rsCliente.next()){
                System.out.println("Nome: " + rsCliente.getString("nome") + ", Email: " + rsCliente.getString("email"));
            }
            rsCliente.close();

            System.out.println("\n=== Usuários CORRETOR ===");
            ResultSet rsCorretor = stmt.executeQuery("SELECT nome, email FROM Usuario WHERE tipo_usuario='" + tipoCorretor + "'");
            while(rsCorretor.next()){
                System.out.println("Nome: " + rsCorretor.getString("nome") + ", Email: " + rsCorretor.getString("email"));
            }
            rsCorretor.close();

            stmt.close();
            conn.close();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
