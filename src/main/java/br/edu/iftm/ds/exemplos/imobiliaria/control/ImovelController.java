package br.edu.iftm.ds.exemplos.imobiliaria.control;

import br.edu.iftm.ds.exemplos.imobiliaria.domain.Imovel;
import br.edu.iftm.ds.exemplos.imobiliaria.repository.ImovelRepository;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;
import java.util.Optional;

@RestController
@RequestMapping("/api/imoveis")
public class ImovelController {

    private final ImovelRepository imovelRepository;

    public ImovelController(ImovelRepository imovelRepository) {
        this.imovelRepository = imovelRepository;
    }

    @GetMapping
    public List<Imovel> getAllImoveis() {
        return imovelRepository.findAll();
    }

    @GetMapping("/{id}")
    public ResponseEntity<Imovel> getImovelById(@PathVariable Integer id) {
        Optional<Imovel> imovel = imovelRepository.findById(id);
        return imovel.map(ResponseEntity::ok)
                .orElse(ResponseEntity.notFound().build());
    }

    @PostMapping
    public Imovel createImovel(@RequestBody Imovel imovel) {
        return imovelRepository.save(imovel);
    }

    @PutMapping("/{id}")
    public ResponseEntity<Imovel> updateImovel(@PathVariable Integer id, @RequestBody Imovel imovelDetails) {
        Optional<Imovel> imovelOptional = imovelRepository.findById(id);
        if (!imovelOptional.isPresent()) {
            return ResponseEntity.notFound().build();
        }
        Imovel imovel = imovelOptional.get();
        imovel.setEndereco(imovelDetails.getEndereco());
        imovel.setPreco(imovelDetails.getPreco());
        imovel.setDescricao(imovelDetails.getDescricao());
        Imovel updatedImovel = imovelRepository.save(imovel);
        return ResponseEntity.ok(updatedImovel);
    }

    @DeleteMapping("/{id}")
    public ResponseEntity<Void> deleteImovel(@PathVariable Integer id) {
        if (!imovelRepository.existsById(id)) {
            return ResponseEntity.notFound().build();
        }
        imovelRepository.deleteById(id);
        return ResponseEntity.noContent().build();
    }
}
