package br.edu.iftm.ds.exemplos.imobiliaria.control;

import br.edu.iftm.ds.exemplos.imobiliaria.domain.Usuario;
import br.edu.iftm.ds.exemplos.imobiliaria.dto.AuthRequest;
import br.edu.iftm.ds.exemplos.imobiliaria.dto.AuthResponse;
import br.edu.iftm.ds.exemplos.imobiliaria.repository.UsuarioRepository;
import br.edu.iftm.ds.exemplos.imobiliaria.Service.UsuarioService;
import br.edu.iftm.ds.exemplos.imobiliaria.config.JwtUtil;
import org.springframework.http.ResponseEntity;
import org.springframework.security.crypto.bcrypt.BCryptPasswordEncoder;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/api/v1/auth")
public class AuthController {

    private final UsuarioRepository userRepo;
    private final UsuarioService userService;
    private final JwtUtil jwtUtil;
    private final BCryptPasswordEncoder encoder = new BCryptPasswordEncoder();

    public AuthController(UsuarioRepository userRepo, UsuarioService userService, JwtUtil jwtUtil) {
        this.userRepo = userRepo;
        this.userService = userService;
        this.jwtUtil = jwtUtil;
    }

    // Registro de usuário
    @PostMapping("/register")
    public ResponseEntity<?> register(@RequestBody Usuario u) {
        if (userRepo.findByLoginUsu(u.getLoginUsu()).isPresent()) {
            return ResponseEntity.badRequest().body("Login já existe");
        }
        // Senha será criptografada no service
        Usuario savedUser = userService.save(u);
        return ResponseEntity.ok(savedUser);
    }

    // Login do usuário
    @PostMapping("/login")
    public ResponseEntity<?> login(@RequestBody AuthRequest req) {
        var opt = userRepo.findByLoginUsu(req.getLogin());
        if (opt.isEmpty()) {
            return ResponseEntity.status(401).body("Credenciais inválidas");
        }

        var user = opt.get();
        if (!encoder.matches(req.getPassword(), user.getSenhaUsu())) {
            return ResponseEntity.status(401).body("Credenciais inválidas");
        }

        String token = jwtUtil.generateToken(user.getLoginUsu());
        return ResponseEntity.ok(new AuthResponse(token));
    }
}