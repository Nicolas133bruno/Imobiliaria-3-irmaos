package br.edu.iftm.ds.exemplos.imobiliaria.control;
import br.edu.iftm.ds.exemplos.imobiliaria.domain.Perfil;
import br.edu.iftm.ds.exemplos.imobiliaria.repository.PerfilRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;
import java.util.Optional;

@RestController
@RequestMapping("/api/perfis")
public class PerfilController {

    @Autowired
    private PerfilRepository perfilRepository;

    @GetMapping
    public List<Perfil> getAllPerfis() {
        return perfilRepository.findAll();
    }

    @GetMapping("/{id}")
    public ResponseEntity<Perfil> getPerfilById(@PathVariable Integer id) {
        Optional<Perfil> perfil = perfilRepository.findById(id);
        return perfil.map(ResponseEntity::ok)
                .orElse(ResponseEntity.notFound().build());
    }

    @PostMapping
    public Perfil createPerfil(@RequestBody Perfil perfil) {
        return perfilRepository.save(perfil);
    }

    @PutMapping("/{id}")
    public ResponseEntity<Perfil> updatePerfil(@PathVariable Integer id, @RequestBody Perfil perfilDetails) {
        Optional<Perfil> perfilOptional = perfilRepository.findById(id);
        if (!perfilOptional.isPresent()) {
            return ResponseEntity.notFound().build();
        }
        Perfil perfil = perfilOptional.get();
        perfil.setTipo_perf(perfilDetails.getTipo_perf());
        Perfil updatedPerfil = perfilRepository.save(perfil);
        return ResponseEntity.ok(updatedPerfil);
    }

    @DeleteMapping("/{id}")
    public ResponseEntity<Void> deletePerfil(@PathVariable Integer id) {
        if (!perfilRepository.existsById(id)) {
            return ResponseEntity.notFound().build();
        }
        perfilRepository.deleteById(id);
        return ResponseEntity.noContent().build();
    }
}